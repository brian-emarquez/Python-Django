from .listunspent import listunspentTX


def formatOuputfromTuple(addresses):
    """
    function for format the output
    """
    addressesOupts = dict()
    for address, amount in addresses:
        if address in addressesOupts:
            addressesOupts[address] = addressesOupts[address] + amount
        else:
            addressesOupts[address] = amount

    for key in addressesOupts:
        addressesOupts[key] = f"{addressesOupts[key]:.8f}"

    return addressesOupts


def createRawTx(rpc, infoTx, params):
    """
    Create a transaction spending the given inputs and creating new outputs.
    Returns hex-encoded raw transaction.
    """

    response = {
        'status': '',
        'message': 'Estamos trabajando'
    }
    componyWallet = params['companyAddressWallet']

    # Validate Addressess
    if rpc.validateaddress(infoTx['addressOrigin'])['isvalid'] is False:
        response['status'] = 'error'
        response['message'] = 'AddressOrigin  invalid'
        return response

    if rpc.validateaddress(infoTx['addressRecipient'])['isvalid'] is False:
        response['status'] = 'error'
        response['message'] = 'AddressRecipient invalid'
        return response

    if componyWallet:
        if rpc.validateaddress(componyWallet)['isvalid'] is False:
            response['status'] = 'error'
            response['message'] = 'companyAddressWallet invalid'
            return response

    if params['minerFee'] <= 0:
        response['status'] = 'error'
        response['message'] = 'Miner fee cannot be 0 or lest'
        return response

    expenses = infoTx['amount'] + params['gain'] + params['minerFee']

    # tx unspent
    respUtxos = listunspentTX(infoTx['addressOrigin'], infoTx['net'], expenses)
    if respUtxos['status'] == 'error':
        return respUtxos

    utxos = respUtxos['data']
    if not utxos:
        response['status'] = 'error'
        response['message'] = 'Not enough to spend'
        return response

    inputs = []

    # INPUTS
    amountAvailable = 0
    for utxo in utxos:
        inputs.append({
            "txid": utxo['txid'],
            "vout": utxo['vout']
        })
        amountAvailable += utxo['amount']

    # OUPUTS
    addresses = []

    # send destination
    addresses.append((infoTx['addressRecipient'], infoTx['amount']))

    # send componyWallet
    if componyWallet:
        addresses.append((componyWallet, params['gain']))  # addrescompany

    # if there is a return of doge
    if amountAvailable - expenses > 0.000005:
        addresses.append((infoTx['addressOrigin'], amountAvailable - expenses))
    else:
        params['minerFee'] += amountAvailable - expenses

    outputs = formatOuputfromTuple(addresses)

    # createTransactions
    try:
        tx_hex = rpc.createrawtransaction(inputs, outputs)
    except:
        response['status'] = 'error'
        response['message'] = 'Error in createrawtransaction'
        return response

    response['status'] = 'successful'
    response['message'] = 'Createrawtransaction'
    response['data'] = {
        'tx_hex': tx_hex,
        'utxos': utxos,
        'amountAvailable': amountAvailable
    }
    return response