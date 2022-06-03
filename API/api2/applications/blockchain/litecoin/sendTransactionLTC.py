from decimal import Decimal
from .jsonrpc import jsrpc
from .createTransactionLTC import createTransactionLTC
from .signTransactionLTC import signTransactionLTC


def sendrawtransaction(rpc, hash_hex):
    """
    Method to send LTC transaction using RPC connection 
    send transaction through the node
    Reference
        https://developer.bitcoin.org/reference/rpc/sendrawtransaction.html
    """

    response = {
        'status': '',
        'message': ''
    }
    try:
        txraw = rpc.sendrawtransaction(hash_hex)
    except:
        response['status'] = 'error'
        response['message'] = 'Error in sendrawtransaction'
        return response

    response['status'] = 'successful'
    response['message'] = 'sendrawtransaction'
    response['data'] = {'tx_hex': txraw
                        }
    return response


def validateTransaction(rpc, hash_hex, dataInfo):
    """
    validate a transaction with the decoderawtransaction function rpc
    """
    response = {
        'status': 'successful',
        'message': 'correct !'
    }

    result = rpc.decoderawtransaction(hash_hex)

    input_b = False
    for input in dataInfo['data']['inputs']:
        tx_id = input['txid']
        vout = input['vout']
        for v_in in result['vin']:
            if tx_id == v_in['txid'] and vout == v_in['vout']:
                input_b = True

    output_val = []
    for idx, value in enumerate(dataInfo['data']['outputs']):
        key = list(value.keys())[0]
        for raw_dict in result['vout']:
            if (raw_dict['scriptPubKey']['addresses'][0] == key and
                    raw_dict['value'] == Decimal(value[key])):

                output_val.append(True)

    verifyReturn = True
    for value in output_val:
        verifyReturn = verifyReturn and value

    if not input_b or not verifyReturn:
        response['status'] = 'error'
        response['message'] = 'Error in input or output'

    return response


def sendTransactionLTC(addressOrigin, addressRecipient, amount, params):
    """
        Method to send LTC transaction using RPC connection 
    """

    response = {
        'status': '',
        'message': 'Estamos trabajando'
    }

    createdTxInfo = {
        'addressOrigin': addressOrigin,
        'addressRecipient': addressRecipient,
        'amount': amount,
    }

    activate, rpc = jsrpc(params['net'])
    if activate is False:
        response['status'] = 'error'
        response['message'] = 'Error on connection node LTC !'
        return response

    resCreatedTX = createTransactionLTC(rpc, createdTxInfo, params)
    if resCreatedTX['status'] == 'error':
        return resCreatedTX

    responseSigned = signTransactionLTC(rpc, resCreatedTX['data'], params)
    if responseSigned['status'] == 'error':
        return responseSigned

    hash_hex = responseSigned['data']['hex']
    responseValidet = validateTransaction(rpc, hash_hex, resCreatedTX)

    if responseValidet['status'] == 'successful':
        responseSend = sendrawtransaction(rpc, hash_hex)
        if responseSend['status'] == 'error':
            return responseSend
        else:
            response['status'] = 'successful'
            response['message'] = 'transaction sent'
            response['data'] = responseSend['data']
            return response
    else:
        return responseValidet
