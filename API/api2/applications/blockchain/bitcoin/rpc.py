import json
import environs
import requests

env = environs.Env()
env.read_env(".env.access") 

def rpc(net, method, params=[]):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 0,
        "method": method,
        "params": params
    })
    if net == 'testnet':
        URL = env.str("URL_BTC_TEST")
        USER = env.str("USER_BTC_TEST")
        PASSWORD = env.str("PASSWORD_BTC_TEST")
        
    else:
        URL = env.str("URL_BTC")
        USER = env.str("USER_BTC")
        PASSWORD = env.str("PASSWORD_BTC")
        
    return requests.post(
            URL,
            auth=(USER, PASSWORD),
            data=payload).json()
