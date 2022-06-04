import json
import requests
import logging
import decimal
from functools import partial
from pprint import pprint
from decimal import Decimal

class ETHRPC(object):
    
    def __init__(self, url):
        self.idcount = 0
        self.url = url
        #self.rpcuser = rpcuser
        #self.rpcpassword = rpcpassword

    def __getattr__(self, name):
        return partial(self.call, name)

    def call(self, method, *params):
        
        c = self.idcount
        self.idcount += 1
        logging.debug("calling ethereumcoind {} with params {}".format(method, params))
        
        v = requests.post(
            self.url,
            #auth=(self.rpcuser, self.rpcpassword),
            headers={ 'Content-Type': 'application/json' },
            json={"version": "2.0", "method": method, "params": params, "id": c},
        ).text

        logging.debug("got response from ethereumcoind: " + v)
        resp = json.loads(v, parse_float=decimal.Decimal)

        if "error" in resp and resp["error"] is not None:
            raise JSONRPCError(resp["error"])

        if "result" not in resp:
            raise JSONRPCError({"code": -343, "message": "missing JSON-RPC result"})

        return resp["result"]

class JSONRPCError(Exception):
    pass


def jsrpc():
    PORT = 8545 
    """USER = 'test'
    PASSWORD = 'test123'"""
    #URL = f"http://161.97.114.244:{PORT}"
    #URL = f"http://127.0.0.1:{PORT}"
    URL = f"https://ropsten.infura.io/v3/dff9133abc8c4869be4a218876136c9a"
    
    rpc = ETHRPC(URL)
    activate = False
    try:
        #balance = rpc.eth_gasPrice()
        balance = rpc.net_listening(
            
        )
        activate=True
        return activate,rpc
    except:
        return activate,''
    
activate, rpc = jsrpc()
print(rpc.eth_accounts())
#print(rpc.eth_getBalance("0x9f1099b301716892d17d576387027cE5B73E2c20", "latest"))
#print(rpc.eth_gasPrice())
#print("net listening: ",rpc.net_listening())


