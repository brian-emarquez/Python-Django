from decimal import Decimal
from .models import Transaction, Input
from .rpc import rpc
from .unspentTransactions import getUnspentTransactionTestnet
from .unspentTransactions import (getUnspentTransactionTestnetApiSoChain,
                                  getUnspentTransaction)


def outputsformat(AddressesTuple):
    """ function to format the output """
    addresses_oupts = dict()
    for address, amount in AddressesTuple:
        if address in addresses_oupts:
            addresses_oupts[address] += amount
        else:
            addresses_oupts[address] = amount

    outputs = []
    for address in addresses_oupts:
        outputs.append({address: float(addresses_oupts[address])})
    return outputs


def createTransactionTestnet(data, fees):
    """
    Method to createrawwtransactions to BTC using testnet: 
    The min amount that we are going to accept is 546 satoshis o
    0.00000546 bitcoin
    """
    response = {
        'status': '',
        'message': 'Error in create transaction, ',
        'data': {}
    }
    if data['amount'] < 0.00000546:
        response['status'] = 'error'
        response['message'] += 'Invalid amount'
        response['message'] += ', should be at least 0.00000546 BTC '
        return response

    amountToSpent = data['amount'] + fees['benefit'] + fees['miner_fee']
    fee = fees['miner_fee']

    # Getting utxos
    try:
        utxos, script = getUnspentTransactionTestnetApiSoChain(
            data['origin'],
            amountToSpent)
    except Exception as ex:
        response['status'] = 'error'
        response['message'] = 'Api to get unspent doesn\'t work'

    if not utxos:
        response['status'] = 'error'
        response['message'] = 'There is not enough balance'
        return response

    transaction = Transaction([], [])
    totalInUtxos = 0

    # Adding inputs
    for utxo in utxos:
        totalInUtxos += utxo['value']
        input = Input(utxo['transaction_hash'], utxo['index'])
        transaction.inputs.append(input.data)

    # Adding outputs
    AddressesTuple = []
    AddressesTuple.append(
        (data['destination'],  Decimal(f"{(data['amount']):.8f}")))
    if fees['company_wallet']:
        AddressesTuple.append(
            (fees['company_wallet'], Decimal(f"{(fees['benefit']):.8f}")))

    # Adding output with devolution
    change = totalInUtxos - amountToSpent

    if change >= 0.00000546:
        AddressesTuple.append((data['origin'], Decimal(f"{change:.8f}")))
    else:
        fee += change
        fees['miner_fee'] = fee

    transaction.outputs = outputsformat(AddressesTuple)

    try:
        resp = rpc("testnet",
                   "createrawtransaction",
                   [transaction.inputs, transaction.outputs]
                   )

        if resp['error']:
            response['status'] = 'error'
            response['message'] += resp['error']['message']
            return response
        else:
            txraw = resp['result']

    except:
        response['status'] = 'error'
        response['message'] += 'Connection to node failed'
        return response
    if txraw:
        response['status'] = 'succes'
        response['message'] = 'Transaction created successfully'
        response['data'] = {
            'status': 'success',
            'txraw': txraw,
            'utxos': utxos,
            'fee': fee,
            'script': script
        }
    else:
        response['status'] = 'error'
    return response


def createTransaction(data, fees):
    """
    Method to createrawwtransactions to BTC using mainnet
    """
    response = {
        'status': '',
        'message': 'Error in create transaction, ',
        'data': {}
    }
    if data['amount'] < 0.00000546:
        response['status'] = 'error'
        response['message'] += 'Invalid amount'
        response['message'] += ', should be at least 0.00000546 BTC '
        return response

    valueToSpent = data['amount'] + fees['benefit'] + fees['miner_fee']
    fee = fees['miner_fee']

    # Getting utxos
    respUtxos = getUnspentTransaction(
            data['origin'],
            valueToSpent)
    
    if respUtxos['status'] == 'error':
        return respUtxos
    
    utxos = respUtxos['data']

    if not utxos:
        response['status'] = 'error'
        response['message'] += 'There is not enough balance'
        return response

    transaction = Transaction([], [])
    totalInUtxos = 0

    # Adding inputs
    for utxo in utxos:
        totalInUtxos += utxo['value']
        input = Input(utxo['tx_hash_big_endian'], utxo['tx_output_n'])
        transaction.inputs.append(input.data)

    # Adding outputs
    conversor = Decimal(0.00000001)
    AddressesTuple = []
    AddressesTuple.append(
        (data['destination'],  Decimal(f"{data['amount']:.8f}")))

    if fees['company_wallet']:
        AddressesTuple.append(
            (fees['company_wallet'],  Decimal(f"{fees['benefit']:.8f}")))

    # Adding output with devolution
    change = totalInUtxos - valueToSpent
    if change >= 0.00000546:
        AddressesTuple.append((data['origin'],  Decimal(f"{change:.8f}")))
    else:
        fee += change
        fees['miner_fee'] = fee

    transaction.outputs = outputsformat(AddressesTuple)

    try:
        resp = rpc("mainnet",
                   "createrawtransaction",
                   [transaction.inputs, transaction.outputs]
                   )
        if resp['error']:
            response['status'] = 'error'
            response['message'] += resp['error']['message']
            return response
        else:
            txraw = resp['result']
    except:
        response['status'] = 'error'
        response['message'] += 'Connection to node failed'
        return response

    if txraw:
        response['status'] = 'succes'
        response['message'] = 'Transaction created successfully'
        response['data'] = {
            'status': 'success',
            'txraw': txraw,
            'utxos': utxos,
            'fee': fee,
        }
    else:
        response['status'] = 'error'
    return response
