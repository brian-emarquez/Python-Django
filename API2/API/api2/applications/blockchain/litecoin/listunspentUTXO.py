from decimal import Decimal
from cryptos import Litecoin


def listUnspent(net, address):
    """
    function to extract the entries to be spent per address 
    with the cryptos library
    """
    if net == 'testnet':
        c = Litecoin(testnet=True)
    elif net == 'mainnet':
        c = Litecoin(mainnet=True)

    if c:
        inputs = c.unspent(address)

    result = []
    conversor = Decimal(0.00000001)
    amountDisponible = 0
    if inputs:
        for input in inputs:
            output = input['output']
            value = input['value']
            idx_c = output.find(':')
            result.append({
                'txid': output[:idx_c],
                'vout': int(output[idx_c + 1:]),
                'amount': Decimal(f"{value*conversor:.8f}")
            })
            amountDisponible += Decimal(f"{value*conversor:.8f}")

    return result


def listunspentUTXO(rpc, address, net, target):
    """
    function to control the listUnspent function 
    """

    response = {
        'status': '',
        'message': ''
    }
    try:
        txuos = listUnspent(net, address)
    except Exception as ex:
        response['status'] = 'error'
        response['message'] = 'Api to get unspent doesn\'t work'
        return response

    utxos = coinSelection(txuos, target)
    response['status'] = 'successful'
    response['data'] = utxos

    return response


def coinSelection(utxos, target):
    """
    Method to obtain the best set of utxos sortedy descending
    """

    bestset = []
    sum = 0
    smallCoins = []
    maxGreater = []

    utxos.sort(key=lambda x: x['amount'], reverse=True)

    for utxo in utxos:
        # Match Single Check
        if utxo['amount'] == target:
            bestset = [utxo]
            return bestset
        # Sum Of Smaller Checks
        elif utxo['amount'] < target:
            sum += utxo['amount']
            smallCoins.append(utxo)
        # Calculate greater
        elif utxo['amount'] > target:
            maxGreater = [utxo]

    if sum == target:
        return smallCoins
    elif maxGreater:
        return maxGreater
    elif sum > target:
        bestset_ = []
        sum_ = 0
        for utx in smallCoins:
            sum_ += utx['amount']
            bestset_.append(utx)
            if sum_ >= target:
                return bestset_
    else:
        return []
