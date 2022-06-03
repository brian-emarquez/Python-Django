import json
from numpy import rint
import requests
import logging
import environs
from pprint import pprint
from functools import partial
from decimal import Decimal
env = environs.Env()
env.read_env(".env.access") 


class DogeRpc(object):
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
        logging.debug("calling litecoind {} with params {}".format(method, params))
        
        v = requests.post(
            self.url,
            auth=(self.rpcuser, self.rpcpassword),
            json={"version": "1.0", "method": method, "params": params, "id": c},
        ).text

        logging.debug("got response from litecoind: " + v)
        resp = json.loads(v, parse_float = Decimal)

        if "error" in resp and resp["error"] is not None:
            raise JSONRPCError(resp["error"])

        if "result" not in resp:
            raise JSONRPCError({"code": -343, "message": "missing JSON-RPC result"})

        return resp["result"]

class JSONRPCError(Exception):
    pass


def rpcdoge(net):
    """
    function to instantiate the rpc according to the network
    """
    if net == 'testnet':
        URL = env.str("URL_DOGE_TESTNET")
        USER = env.str("USER_DOGE_TESTNET" )
        PASSWORD = env.str("PASSWORD_DOGE_TESTNET")
    else:
        URL = env.str("URL_DOGE_MAINNET")
        USER = env.str("USER_DOGE_MAINNET")
        PASSWORD = env.str("PASSWORD_DOGE_MAINNET")
   
    rpc = DogeRpc(URL, USER, PASSWORD)
    activate = False
    try:
        balance = rpc.getbalance()
        activate = True
        return activate,rpc
    except :
        return activate,''