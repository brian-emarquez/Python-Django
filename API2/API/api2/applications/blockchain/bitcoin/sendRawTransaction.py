from .createTransaction import createTransactionTestnet, createTransaction
from .signTransaction import signTransactionTest, signTransaction
from .sendTransaction import sendTransaction


def sendRawTransactionTesnet(data):
    """function that sends the transaction raw through the test network"""

    fees = {
        'miner_fee': data['minerFee'],
        'benefit': data['gain'],
        'company_wallet': data['company_wallet']
    }

    responseCreated = createTransactionTestnet(data, fees)
    if responseCreated['status'] == 'error':
        return responseCreated

    data['minerFee'] = fees['miner_fee']

    responseSigned = signTransactionTest(responseCreated['data'], data)
    if responseSigned['status'] == 'error':
        return responseSigned

    responseSend = sendTransaction(
        responseSigned['data']['txraw'],
        responseCreated['data']['fee'],
        data['net'])

    return responseSend


def sendRawTransactionMainnet(data):
    """function that sends the transaction raw through the main network"""

    fees = {
        'miner_fee': data['minerFee'],
        'benefit': data['gain'],
        'company_wallet': data['company_wallet']
    }
    responseCreated = createTransaction(data, fees)
    if responseCreated['status'] == 'error':
        return responseCreated

    data['minerFee'] = fees['miner_fee']

    responseSigned = signTransaction(responseCreated['data'], data)
    if responseSigned['status'] == 'error':
        return responseSigned

    responseSend = sendTransaction(
        responseSigned['data']['txraw'],
        responseCreated['data']['fee'],
        data['net'])

    return responseSend
