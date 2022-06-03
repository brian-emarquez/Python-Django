import codecs
import json
from decimal import Decimal
from  pprint import pprint

def signTransactionETH(rpc,signInfo, extraInfo):
    """
    Method to signTransactionETH
    Ref https://eth.wiki/json-rpc/API#eth_sendrawtransaction

    """
    response = {
            'status':'',
            'message':'',
    }
    
    utxosToSpent = []
    """for utxo in signInfo['utxos']:
        utxosToSpent.append({                           
                "txid": utxo['txid'],
                "vout": utxo['vout'],
                "scriptPubKey": utxo['scriptPubKey'],
                "redeemScript": utxo['redeemScript'],
                "amount": str(utxo['amount'])
        })"""

    try:
        hexstring = signInfo['tx_hex']
        privateKey = extraInfo['privateKey']
        tx_hex = rpc.signrawtransactionwithkey(hexstring,[privateKey])#utxosToSpent
    except:
        response['status'] = 'error'
        response['message'] = 'Error in signrawtransactionwithkey'
        return response
        
    response['status'] = 'successful'
    response['message'] = 'signrawtransactionwithkey'
    response['data'] = tx_hex
    return response
