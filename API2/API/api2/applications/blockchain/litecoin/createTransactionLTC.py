from .listunspentUTXO import listunspentUTXO


def preCalculationInputsOuputs(rpc, txInfo, extraInfo):
    response = {
        'status': '',
        'message': ''
    }
    companyWallet = extraInfo['companyAddressWallet']

    # Validate Addresses
    if rpc.validateaddress(txInfo['addressOrigin'])['isvalid'] is False:
        response['status'] = 'error'
        response['message'] = 'AddressOrigin  invalid'
        return response

    if rpc.validateaddress(txInfo['addressRecipient'])['isvalid'] is False:
        response['status'] = 'error'
        response['message'] = 'AddressRecipient invalid'
        return response

    if companyWallet:
        if rpc.validateaddress(companyWallet)['isvalid'] is False:
            response['status'] = 'error'
            response['message'] = 'companyAddressWallet invalid'
            return response

    if extraInfo['minerFee'] <= 0:
        response['status'] = 'error'
        response['message'] = 'Miner fee cannot be 0 or lest'
        return response

    expenses = txInfo['amount'] + extraInfo['gain'] + extraInfo['minerFee']

    respUtxos = listunspentUTXO(rpc, txInfo['addressOrigin'],
                                extraInfo['net'], expenses)
    if respUtxos['status'] == 'error':
        return respUtxos

    utxos = respUtxos['data']
    if not utxos:
        response['status'] = 'error'
        response['message'] = 'Not enough to spend'
        return response

    if type(utxos) == tuple:
        utxos = utxos[0]

    inputs = []
    outputs = []

    # INPUTS
    amountAvailable = 0
    for utxo in utxos:
        if utxo:
            inputs.append({
                "txid": utxo['txid'],
                "vout": utxo['vout']
            })
            amountAvailable += utxo['amount']
    # OUPUTS
    addresses = []
    addresses.append((txInfo['addressRecipient'], txInfo['amount']))  # DESTINO

    if companyWallet:
        addresses.append((companyWallet, extraInfo['gain']))  # addrescompany
    if amountAvailable - expenses > 0.000005:
        addresses.append((txInfo['addressOrigin'], amountAvailable - expenses))
    else:
        extraInfo['minerFee'] += amountAvailable - expenses

    addressesOupts = dict()
    for address, amount in addresses:
        if address in addressesOupts:
            addressesOupts[address] += amount
        else:
            addressesOupts[address] = amount

    for address in addressesOupts:
        outputs.append({address: float(f"{addressesOupts[address]:.8f}")})

    response['status'] = 'successful'
    response['message'] = 'correct !'
    response['data'] = {
        'inputs': inputs,
        'outputs': outputs,
        'utxos': utxos,
        'amountAvailable': amountAvailable
    }
    return response


def createTransactionLTC(rpc, txInfo, extraInfo):
    """
    function for createraw transactions
    reference 
     https://developer.bitcoin.org/reference/rpc/createrawtransaction.html
    """
    response = {
        'status': '',
        'message': ''
    }

    # CALCULATION INPUTS - OUPUTS
    respIO = preCalculationInputsOuputs(rpc, txInfo, extraInfo)

    if respIO['status'] == 'error':
        return respIO

    inputs = respIO['data']['inputs']
    outputs = respIO['data']['outputs']

    try:
        txhex = rpc.createrawtransaction(inputs, outputs)
    except:
        response['status'] = 'error'
        response['message'] = 'Error in createrawtransaction'
        return response

    response['status'] = 'successful'
    response['message'] = 'Createrawtransaction'
    response['data'] = respIO['data']
    response['data']['tx_hex'] = txhex

    return response
