import json
import logging
from decimal import Decimal
from functools import partial

import environs
import requests

env = environs.Env()
env.read_env(".env.access") 



class LtcRpc(object):
    """ 
    Autor: Yessica Chuctaya 
    Fecha de creación: 2021
    Fecha de modificación:2022
    Descripción:
        01 - Create class
    """

    def __init__(self, url, rpcuser, rpcpassword):
        self.idcount = 0
        self.url = url
        self.rpcuser = rpcuser
        self.rpcpassword = rpcpassword

    def __getattr__(self, name):
        return partial(self.call, name)

    def call(self, method, *params):
        c = self.idcount
        self.idcount += 1
        logging.debug(
            "calling litecoind {} with params {}".format(method, params))

        v = requests.post(
            self.url,
            auth=(self.rpcuser, self.rpcpassword),
            json={"version": "1.1", "method": method,
                  "params": params, "id": c},
        ).text

        logging.debug("got response from litecoind: " + v)
        resp = json.loads(v, parse_float=Decimal)

        if "error" in resp and resp["error"] is not None:
            raise JSONRPCError(resp["error"])

        if "result" not in resp:
            raise JSONRPCError(
                {"code": -343, "message": "missing JSON-RPC result"})

        return resp["result"]


class JSONRPCError(Exception):
    pass


def jsrpc(net):
    """ 
        function to instantiate the rpc according to the network 
    """
    if net == 'testnet':
        URL = env.str("URL_LTC_TEST")
        USER = env.str("USER_LTC_TEST" )
        PASSWORD = env.str("PASSWORD_LTC_TEST")
    else:
        URL = env.str("URL_LTC_MAIN")
        USER = env.str("USER_LTC_MAIN")
        PASSWORD = env.str("PASSWORD_LTC_MAIN")
    
    rpc = LtcRpc(URL, USER, PASSWORD)
    activate = False
    try:
        balance = rpc.getbalance()
        activate = True
        return activate, rpc
    except:
        return activate, ''
