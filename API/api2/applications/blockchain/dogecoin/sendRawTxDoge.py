from .conect import rpcdoge
from .createTXDoge import createRawTx


def signRawTransaction(rpc, data, params):
    """
    function to sign the created transaction in doge
    """
    response = {
        'status': '',
        'message': ''
    }

    hexstring = data['tx_hex']
    previous_transactions = []
    private_keys = params['private_key']

    try:
        tx_hex = rpc.signrawtransaction(hexstring, [], [private_keys])
    except:
        response['status'] = 'error'
        response['message'] = 'Error in signrawtransaction'
        return response

    response['status'] = 'successful'
    response['message'] = 'signrawtransaction'
    response['data'] = tx_hex
    return response


def sendRawTx(rpc, data):
    """
    Method to send DOGE transaction using RPC connection 
    Ref https://developer.bitcoin.org/reference/rpc/sendrawtransaction.html
    """
    response = {
        'status': '',
        'message': ''
    }
    try:
        hexstr = data['hex']
        txraw = rpc.sendrawtransaction(hexstr)

    except:
        response['status'] = 'error'
        response['message'] = 'Error in sendrawtransaction'
        return response

    response['status'] = 'successful'
    response['message'] = 'sendrawtransaction'
    response['data'] = {
        'tx_hex': txraw
    }
    return response


def sendTransactionDoge(data_req):
    """
    Function to perform the whole process of transaction in dogecoin 
        1.- connect to rpc 
        2.- create transaction
        3.- sign transaction 
        4.- send the transaction through the node 
    """
    activate, rpc = rpcdoge(data_req['net'])
    response = {
        'status': '',
        'message': ''
    }
    info = {
        'addressOrigin': data_req['origin'],
        'addressRecipient': data_req['destination'],
        'private_key': data_req['private'],
        'amount': data_req['amount'],
        'net': data_req['net']
    }

    params = {
        'companyAddressWallet': data_req['company_wallet'],
        'gain': data_req['gain'],
        'minerFee': data_req['minerFee']
    }

    if not activate:
        response['status'] = 'error'
        response['message'] = 'Error on connection node DOGE !'
        return response

    resCreatedTX = createRawTx(rpc, info, params)
    if resCreatedTX['status'] == 'error':
        return resCreatedTX

    responseSigned = signRawTransaction(rpc, resCreatedTX['data'], info)
    if responseSigned['status'] == 'error':
        return responseSigned

    responseSend = sendRawTx(rpc, responseSigned['data'])

    data_req['minerFee'] = params['minerFee']
    return responseSend
