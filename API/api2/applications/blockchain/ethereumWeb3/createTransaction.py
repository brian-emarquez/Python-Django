from cmath import e
from logging import exception
from pprint import pprint
from applications.cryptocurrencies.models import Cryptocurrencies
from .web3Connect import web3EthConnect
from .sendEthereum import sendTxEthereum
from decimal import Decimal


"""
    Description: in this part we control errors, calculate operations and 
    then send them to the transactions. 🚀
    Author: Brian Enrique Marquez Inca Roca
    Creation date: 2021
    Last modification: 29/01/2022
"""


def calculateGasPrice(gasLimit, MinerFee):
    """
    function that calculates the gas in Ethereum
    """

    MinerFee = MinerFee / 2
    cryptocurrency = Cryptocurrencies.objects.get(Symbol='ETH')
    gasLimit = int(cryptocurrency.GasLimit)  # gasLimit = 21000
    gasPrice = MinerFee / gasLimit
    gasPrice = gasPrice / Decimal(0.000000000000000001)
    gasPrice = int(gasPrice)

    return gasPrice


def importWalletv2(data):
    """
    function to create an attraction and import transaction
    """

    response = {
        'status': '',
        'messages': ''
    }
    # net = data['net']
    responseEth = web3EthConnect(data['net'])
    if responseEth['status'] == 'Error':
        response['status'] = 'error'
        response['message'] = 'connection fail node eth'
        return response

    web3node = responseEth['web3node']
    if web3node.isAddress(data['addressOrigin']) is False:
        response['status'] = 'error'
        response['messages'] = 'The origin address is not valid'
        return response

    if web3node.isAddress(data['addressRecipient']) is False:
        response['status'] = 'error'
        response['messages'] = 'The destination ad dress is not valid'
        return response

    availableAmount = web3node.eth.get_balance(data['addressOrigin'])
    expenses = data['amount'] + data['minerFee']

    if expenses > availableAmount:
        response['status'] = 'error'
        response['messages'] = 'insufficient balance'
        return response

    if data['net'] == "rospten":
        chainId = 3
    elif data['net'] == "mainnet":
        chainId = 1

    nonce = web3node.eth.getTransactionCount(data['addressOrigin'])
    print(data, "\n")

    tx1 = {
        'chainId': chainId,
        'nonce': nonce,
        'from': data['addressOrigin'],
        'to': data['addressRecipient'],
        'value': web3node.toWei(data['amount'], 'ether'),
        'gas':  21000,
        'gasPrice': calculateGasPrice(21000, 2*data['minerFee'])
    }

    signed_tx = web3node.eth.account.signTransaction(tx1, data['privateKey'])
    print(".:.")
    tx_hash = web3node.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(":::")
    print(tx_hash)

    response['data'] = web3node.toHex(tx_hash)
    return response


def createTransactionEth(data):
    """
    Method to create trasaction to ETH
    """

    response = {
        'status': '',
        'messages': ''
    }

    addressOrigin = data['addressOrigin']
    addressRecipient = data['addressRecipient']

    """
    the hexadecimal is added to addresses that do not have
    """

    if (addressOrigin.find('0x') == -1):
        addressOrigin = '0x' + data['addressOrigin']
        data['addressOrigin'] = addressOrigin

    if (addressRecipient.find('0x') == -1):
        addressRecipient = '0x' + data['addressRecipient']
        data['addressRecipient'] = addressRecipient

    responseEth = web3EthConnect(data['net'])

    if responseEth['status'] == 'Error':
        response['status'] = 'error'
        response['message'] = 'connection fail node eth'
        return response

    web3node = responseEth['web3node']

    if web3node.isAddress(data['addressOrigin']) is False:
        response['status'] = 'error'
        response['messages'] = 'The origin address is not valid'
        return response

    if web3node.isAddress(data['addressRecipient']) is False:
        response['status'] = 'error'
        response['messages'] = 'The destination ad dress is not valid'
        return response

    """
    Balance Account Eth
    """

    availableAmount = web3node.eth.get_balance(data['addressOrigin'])
    availableAmount = Decimal(f"{Decimal(availableAmount):.8f}")

    """
    Mining payment and profit
    """
    expenses = data['amount'] + data['gain'] + data['minerFee']

    if expenses > availableAmount:
        response['status'] = 'error'
        response['messages'] = 'insufficient balance'
        return response

    """
    shipping to the customer, Exchange
    """

    amountTmp = data['amount']
    if data['addressRecipient'] == data['walletCompany']:
        amountTmp = amountTmp + data['gain']
        data['gain'] = 0
        data['walletCompany'] = ''

    nonce = web3node.eth.get_transaction_count(data['addressOrigin'])

    cryptocurrency = Cryptocurrencies.objects.get(Symbol='ETH')
    gasLimit = int(cryptocurrency.GasLimit)  # gasLimit = 21000

    dataSend = {
        'addressOrigin': data['addressOrigin'],
        'addressRecipient': data['addressRecipient'],
        'amount': amountTmp,
        'privateKey': data['privateKey'],
        'net': data['net'],
        'nonce': nonce,
        'gasLimit': gasLimit,
        'gasPrice': calculateGasPrice(gasLimit, data['minerFee'])
    }
    """
    Funtion SendTxEthreum
    """
    hassend = sendTxEthereum(dataSend, web3node)
    print(dataSend, "\n")

    """
    Remittance of earnings to the company
    """
    hassendCompany = ''

    if data['gain'] != 0 and data['walletCompany'] != '':
        dataSendWallet = {
            'addressOrigin': data['addressOrigin'],
            'addressRecipient': data['walletCompany'],
            'amount': data['gain'],
            'privateKey': data['privateKey'],
            'net': data['net'],
            'nonce': nonce + 1,
            'gasLimit': gasLimit,
            'gasPrice': calculateGasPrice(gasLimit, data['minerFee'])
        }

        print(dataSendWallet, "\n")
        hassendCompany = sendTxEthereum(dataSendWallet, web3node)

    response['status'] = 'successful'
    response['messages'] = 'transaction sent'

    if hassendCompany == '':
        response['data'] = {
            'HashSendClient': hassend
        }
    else:
        response['data'] = {
            'HashSendCompany': hassendCompany,
            'HashSendClient': hassend
        }
        print("response: ", response)
    return response
