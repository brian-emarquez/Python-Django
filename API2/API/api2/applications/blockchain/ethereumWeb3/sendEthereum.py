from decimal import *
from unicodedata import decimal

"""
    Description: Method to sendEthereum shipping, signing and transmission
    to the network🚀
    Author: Brian Enrique Marquez Inca Roca
    Creation date: 2021
    Last modification: 29/01/2022
"""

def sendTxEthereum(data, web3node):
    
    #GasPrice()
    nonceTrue = True
    count = 0
        
    while nonceTrue is True and count < 10:
        try:

            response = {
                'status': '',
                'messages': ''
            }

            if data['net'] == "rospten":
                chainId = 3
            elif data['net'] == "mainnet":
                chainId = 1
            

            tx = {
                'chainId': chainId,
                'nonce': data["nonce"],
                'from': data['addressOrigin'],
                'to': data['addressRecipient'],
                'value': web3node.toWei(data['amount'], 'ether'),
                'gas':  data['gasLimit'],
                'gasPrice': data['gasPrice']
                #'gasPrice' : web3node.toWei(50, 'gwei')
            }
            """
            in this part the signature is made and in the sending of 
            the transaction
            """
            signed_tx = web3node.eth.account.signTransaction(
                tx, data['privateKey'])
            print(".:.")
            tx_hash = web3node.eth.sendRawTransaction(signed_tx.rawTransaction)
            print("::.")
            nonceTrue = False
            return web3node.toHex(tx_hash)
        except:
            response['status'] = 'error'
            response['message'] = 'transaction failed'
            data["nonce"] += 1
            count += 1
    return response
