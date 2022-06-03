from decimal import Decimal
import requests


def apiSochainUnspent(net, address):
    """
    function for extracting from api the inputs to be spent of address doge
    """
    response = {
        'status': '',
        'message': ' '
    }

    if net == 'testnet':
        network = 'DOGETEST'
    else:
        network = 'DOGE'

    resp = requests.get(
        f'https://chain.so/api/v2/get_tx_unspent/{network}/{address}')

    if resp.status_code == 200:
        data = resp.json()['data']
        txs = []
        for tx in data['txs']:
            txs.append({'vout': int(tx['output_no']),
                        'txid': tx['txid'],
                        'amount': Decimal(tx['value']),
                        'script_hex': tx['script_hex'],
                        })
        response['status'] = 'sucessful'
        response['data'] = txs
        return response
    else:
        response['status'] = 'error'
        response['message'] += 'Api to get unspent doesn\'t work'


def coinSelection(utxos, target):
    """
    Method to obtain the best set of utxos 
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
        if utxo['amount'] < target:
            sum += utxo['amount']
            smallCoins.append(utxo)
        # Calculate greater
        if utxo['amount'] > target:
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


def listunspentTX(address, net, expenses):
    """
        function to control the listUnspent function and 
        select the best combination 
    """

    response = {
        'status': '',
        'message': ' '
    }

    resp = apiSochainUnspent(net, address)

    if resp['status'] == 'error':
        return resp

    utxos = resp['data']
    if utxos:
        utxos = coinSelection(utxos, expenses)

    response['status'] = 'sucessful'
    response['data'] = utxos
    return response
