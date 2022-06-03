import json
import requests
from decimal import Decimal
from functools import partial


class Rpc:
    """
    Author: Yessica Chuctaya
    Modification date: 02/03/2022
    Description: 
    01 - Create class CryptoSyscoin
    """

    response = {
        'status': '',
        'message': '',
        'data': {}
    }

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
        try:
            result = requests.post(
                self.url,
                auth=(self.rpcuser, self.rpcpassword),
                json={"jsonrpc": "1.0", "method": method,
                      "params": params, "id": c},
            )
            resp = json.loads(result.text, parse_float=Decimal)
            return resp

        except Exception as e:
            response = {
                'result': '',
                'error': {
                    'message': e
                }
            }
            return response
