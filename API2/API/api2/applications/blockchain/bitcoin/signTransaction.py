from decimal import Decimal
from .rpc import rpc


def signTransactionTest(txcreated, data):
    """
    Method to createrawwtransactions
        txid': transaction hash,
        vout': orden in utxos,
        scriptPubKey': Unlock script,
        redeemScript': public key,
        amount': Amount in bitcoins
    """
    response = {
        'status': '',
        'message': ' Error en Signrawtransaction ',
        'data': ''
    }
    utxosToSpent = []

    for utxo in txcreated['utxos']:
        utxosToSpent.append({
            'txid': utxo['transaction_hash'],
            'vout': utxo['index'],
            'scriptPubKey': txcreated['script'],
            'redeemScript': data['public'],
            'amount': f"{utxo['value']:.8f}"
        })

    # Sign transaction with key
    try:
        resp = rpc(
            "testnet",
            "signrawtransactionwithkey",
            [txcreated['txraw'], [data['private']], utxosToSpent])

        if resp['error']:
            response['status'] = 'error'
            response['message'] += resp['error']['message']
            return response
        else:
            response['status'] = 'success'
            response['message'] = 'Successfull in send transaction'
            txraw = resp['result']['hex']
            response['data'] = {'txraw': txraw}

    except:
        response['status'] = 'error'
        response['message'] += 'Connection to node failed'
        return response

    return response


def signTransaction(txcreated, data):
    """
    Method to createrawwtransactions
        txid':transaction hash,
        vout':orden in utxos,
        scriptPubKey':Unlock script,
        redeemScript': public key,
        amount': Amount in bitcoins
    """
    response = {
        'status': '',
        'message': 'Error in sign transaction, ',
        'data': ''
    }
    utxosToSpent = []

    resp = rpc("mainnet", "validateaddress", [data['origin']])
    if resp['error']:
        response['status'] = 'error'
        response['message'] += resp['error']['message']
        return response
    else:
        validateAddress = resp['result']

    if validateAddress['isvalid'] is True:
        public = validateAddress['scriptPubKey']
        for utxo in txcreated['utxos']:
            utxosToSpent.append({
                'txid': utxo['tx_hash'],
                'vout': utxo['tx_output_n'],
                'scriptPubKey': utxo['script'],
                'redeemScript': public,
                'value': f"{utxo['value']:.8f}"
            })

    # Sign transaction with key
    try:

        resp = rpc(
            "mainnet",
            "signrawtransactionwithkey",
            [txcreated['txraw'], [data['private']]])

        if resp['error']:
            response['status'] = 'error'
            response['message'] += resp['error']['message']
            return response
        else:
            response['status'] = 'success'
            response['message'] = 'Successfull in send transaction'
            txraw = resp['result']['hex']
            response['data'] = {'txraw': txraw}

    except:
        response['status'] = 'error'
        response['message'] += 'Connection to node failed'
        return response

    return response
