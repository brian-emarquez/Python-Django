import math
import requests
from decimal import Decimal


def getUnspentTransaction(address, target):
    """
    Method to obtain unspent transactions for a address
    """
    response = {
        'status': '',
        'message': 'Error in create transaction, ',
        'data': {}
    }
    apiUrl = f'https://blockchain.info/unspent?active={address}'
    responseAPI = requests.get(apiUrl)

    if responseAPI.status_code == 200:
        resp = responseAPI.json()
        utxos = []

        try:
            utxos = coinSelection(resp['unspent_outputs'], target)
        except:
            return utxos
        response['status'] = 'successfull'
        response['data'] = utxos
    else :
        response['status'] = 'error'
        response['message'] = 'Api to get unspent doesn\'t work'
        
    return response


def getUnspentTransactionTestnet(address, target):
    """
    Method to obtain unspent transactions for a address
    Data structure for api.bitaps testnet
    """
    api = 'https://api.blockchair.com/bitcoin/testnet/dashboards/address/'
    response = requests.get(api + address)
    if response.status_code == 200:
        response = response.json()
        data = response['data'][address]
        utxos = []
        script = ''
        try:
            script = data['address']['script_hex']
            utxos = coinSelection(data['utxo'], target)
        except:
            return utxos, script
        return utxos, script


def coinSelection(utxos, target):
    """
    Method to obtain the best set of utxos fro mainnet
    """
    conversor = Decimal(0.00000001)
    bestset = []
    sum = 0
    smallCoins = []
    maxGreater = []

    utxos.sort(key=lambda x: x['value'], reverse=True)

    for utxo in utxos:
        utxo['value'] = Decimal(f"{(utxo['value']*conversor):.8f}")
        if utxo['value'] == target:
            bestset = [utxo]
            return bestset
        elif utxo['value'] < target:
            sum += utxo['value']
            smallCoins.append(utxo)
        elif utxo['value'] > target:
            maxGreater = [utxo]
    if sum == target:
        return smallCoins
    elif maxGreater:
        return maxGreater
    elif sum > target:
        bestset_ = []
        sum_ = 0
        for utx in smallCoins:
            sum_ += utx['value']
            bestset_.append(utx)
            if sum_ >= target:
                return bestset_
    else:
        return []


def formatSoChain(utxos):
    """
        function to format the output of the soChain api
    """
    utxos_ = []
    for element in utxos:
        utxos_.append({
            'transaction_hash': element['txid'],
            'index': element['output_no'],
            'value': float(element['value']),
        })
    return utxos_


def coinSelectionApiSoChain(utxos, target):
    """
    Method to obtain the best set of utxos fro mainnet
    utxo sortedy descending
    """
    bestset = []
    sum = 0
    smallCoins = []
    maxGreater = []

    utxos.sort(key=lambda x: x['value'], reverse=True)

    for utxo in utxos:
        utxo['value'] = Decimal(f"{utxo['value']:.8f}")
        if utxo['value'] == target:
            bestset = [utxo]
            return bestset
        elif utxo['value'] < target:
            sum += utxo['value']
            smallCoins.append(utxo)
        elif utxo['value'] > target:
            maxGreater = [utxo]

    if sum == target:
        return smallCoins
    elif maxGreater:
        return maxGreater
    elif sum > target:
        bestset_ = []
        sum_ = 0
        for utx in smallCoins:
            sum_ += utx['value']
            bestset_.append(utx)
            if sum_ >= target:
                return bestset_
    else:
        return []


def getUnspentTransactionTestnetApiSoChain(address, target):
    """
    Method to obtain unspent transactions for a address
    """
    apiTestUrl = f'https://chain.so/api/v2/get_tx_unspent/BTCTEST/{address}'
    response = requests.get(apiTestUrl)
    if response.status_code == 200:
        response = response.json()
        data = formatSoChain(response['data']['txs'])
        utxos = []
        script = ''
        try:
            script = response['data']['txs'][0]['script_hex']
            utxos = coinSelectionApiSoChain(data, target)
        except:
            return utxos, script
        return utxos, script
