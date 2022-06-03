from decimal import Decimal
from .rpc import rpc


def sendTransaction(rawdata, fee, net):
    """
    Method to send BTC transaction using RPC connection 
    """
    response = {
        'status': '',
        'message': 'Error in send transaction, ',
        'data': ''
    }
    fee = f"{(fee*Decimal(0.00000001)):.8f}"

    try:
        resp = rpc(net, "sendrawtransaction", [rawdata])
        if resp['error']:
            response['status'] = 'error'
            response['message'] += resp['error']['message']
            return response
        else:
            response['status'] = 'success'
            response['message'] = 'Successfull in send transaction'
            txraw = resp['result']
            response['data'] = {'txid': txraw}

    except:
        response['status'] = 'error'
        response['message'] += 'Connection to node failed'
        return response

    return response
