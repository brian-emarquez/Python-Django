def signTransactionLTC(rpc, signInfo, extraInfo):
    """
    Method to sign Transaction in LTC reference 
    https://developer.bitcoin.org/reference/rpc/signrawtransactionwithkey.html

    """
    response = {
        'status': '',
        'message': '',
    }

    try:
        hexstring = signInfo['tx_hex']
        privateKey = extraInfo['privateKey']
        tx_hex = rpc.signrawtransactionwithkey(hexstring,
                                               [privateKey]
                                               # utxosToSpent
                                               )
    except Exception as e:
        response['status'] = 'error'
        response['message'] = 'Error in signrawtransactionwithkey  ' + str(e)
        return response

    response['status'] = 'successful'
    response['message'] = 'signrawtransactionwithkey'
    response['data'] = tx_hex
    return response
