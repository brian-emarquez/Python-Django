from web3 import Web3
from web3.middleware import geth_poa_middleware
#SUBREDES Contract Chain (C-Chain ) 


class CryptoAvalancheC:

    """
    Author: Yessica Chuctaya
    Modification date: 11/03/2022
    Description: 
        01 - Create class ERC20NetworkBase
    """

    node_url = ""  # Red Testnet
    chainId = ""
    url_explorer = ""

    web3 = ""

    def __init__(self, url, chainId, explorer):
        self.node_url = url
        self.chainId = chainId
        self.url_explorer = explorer

        self.web3 = Web3(Web3.HTTPProvider(self.node_url))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

        if self.web3.isConnected() is True:
            print('  Conect url node    ')
        else:
            print('  Failed conect      ')
        print('\n')

    def sendTx(self, net, amount, nonce, addressFrom, addressTo,
               private, minerFee):
        """
        function to send a transaction 
        """
        maxPriorityFeePerGas = self.web3.toWei('2', 'gwei')

        gas = self.web3.eth.estimate_gas({
            'to': addressTo,
            'from': addressFrom,
            'value': self.web3.toWei(amount, 'ether')
        })

        maxFeePerGas = minerFee/gas
        maxFeePerGas = int(maxFeePerGas * 10**(18))

        tx = {
            'nonce': nonce,
            'chainId': self.chainId,
            'gas': gas,
            'to': addressTo,
            'value': self.web3.toWei(amount, 'ether'),
            'maxFeePerGas': maxFeePerGas,
            'maxPriorityFeePerGas': maxPriorityFeePerGas
        }

        # SIGN IN
        signed = self.web3.eth.account.sign_transaction(tx, private)
        # SEND TRX
        try:
            tx_hash = self.web3.eth.send_raw_transaction(signed.rawTransaction)
        except Exception as e:
            print('error', e, '\n')

        hash_ = self.web3.toHex(tx_hash)
        result = self.web3.eth.get_transaction(hash_)
        fee = self.web3.fromWei(result['gasPrice'], 'ether') * gas

        return hash_, fee

    def trySendTx(self, net, amount, nonce, addressFrom, addressTo,
                  private, minerFee):
        """
        function to control the number of attempts to perform a sending 
        transaction default 2
        """
        response = {
            'status': '',
            'message': '',
            'data': ''
        }
        nonceTrue = True
        count = 0
        while nonceTrue is True and count < 2:
            try:
                hash, fee = self.sendTx(net, amount, nonce, addressFrom,
                                        addressTo, private, minerFee)
                nonceTrue = False
                response['status'] = 'successful'
                response['data'] = {
                    'hash': hash,
                    'nonce': nonce,
                    'fee': fee
                }
            except:
                response['status'] = 'error'
                response['message'] = 'transaction failed'
                nonce += 1
                count += 1

        return response

    def transaction(self, net, addressFrom, addressTo, amount, addressCompany,
                    gain, private, minerfee):
        """
        function to perform the transaction process in avalanche
        """
        response = {
            'status': '',
            'message': '',
            'data': ''
        }

        if self.web3.isAddress(addressFrom) is False:
            response['status'] = 'error'
            response['messages'] = 'The origin address is not valid'
            return response

        if self.web3.isAddress(addressTo) is False:
            response['status'] = 'error'
            response['messages'] = 'The destination ad dress is not valid'
            return response

        if self.web3.isAddress(addressCompany) is False:
            response['status'] = 'error'
            response['messages'] = 'The company wallet address is not valid'
            return response

        expenses = amount + gain + minerfee
        expenses = self.web3.toWei(expenses, 'ether')
        availableAmount = self.web3.eth.get_balance(addressFrom)

        if expenses > availableAmount:
            response['status'] = 'error'
            response['messages'] = 'insufficient balance token'
            return response

        nonce = self.web3.eth.get_transaction_count(addressFrom)

        resp = self.trySendTx(net, amount, nonce,
                              addressFrom, addressTo, private, minerfee)
        if resp['status'] == 'error':
            return resp

        hashsend = resp['data']['hash']
        nonce_, fee_send = resp['data']['nonce'], resp['data']['fee']

        resp_ = self.trySendTx(net, gain, nonce_ + 1, addressFrom,
                               addressCompany, private, minerfee)

        if resp_['status'] == 'error':
            return resp_
        hashCompany, fee_company = resp_['data']['hash'], resp_['data']['fee']

        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
            'HashSendCompany': hashCompany,
            'HashSendClient': hashsend,
            'fee': fee_send + fee_company
        }
        return response

    def importBase(self, net, addressFrom, addressTo, amount,
                   private, minerfee):
        """
        function to perform the import process
        """
        response = {
            'status': '',
            'message': '',
            'data': ''
        }
        if self.web3.isAddress(addressFrom) is False:
            response['status'] = 'error'
            response['messages'] = 'The origin address is not valid'
            return response

        if self.web3.isAddress(addressTo) is False:
            response['status'] = 'error'
            response['messages'] = 'The destination ad dress is not valid'
            return response

        expenses = amount + minerfee
        expenses = self.web3.toWei(expenses, 'ether')
        availableAmount = self.web3.eth.get_balance(addressFrom)

        if expenses > availableAmount:
            response['status'] = 'error'
            response['messages'] = 'insufficient balance '
            return response

        addressFromCheck = self.web3.toChecksumAddress(addressFrom)
        nonce = self.web3.eth.get_transaction_count(addressFromCheck)

        resp_ = self.trySendTx(net, amount, nonce,  addressFrom, addressTo,
                               private, minerfee)
        if resp_['status'] == 'error':
            return resp_
        hashsend, fee_ = resp_['data']['hash'], resp_['data']['fee']

        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
            'HashSendClient': hashsend,
            'fee': fee_
        }
        return response

    def exchange(self, net, addressFrom, addressTo, amount, gain,
                 private, minerfee):
        """
        function to perform the export process 
        """
        response = {
            'status': '',
            'message': '',
            'data': ''
        }

        if self.web3.isAddress(addressFrom) is False:
            response['status'] = 'error'
            response['messages'] = 'The origin address is not valid'
            return response

        if self.web3.isAddress(addressTo) is False:
            response['status'] = 'error'
            response['messages'] = 'The destination address is not valid'
            return response

        expenses = amount + gain + minerfee
        expenses = self.web3.toWei(expenses, 'ether')
        availableAmount = self.web3.eth.get_balance(addressFrom)

        if expenses > availableAmount:
            response['status'] = 'error'
            response['messages'] = 'insufficient balance '
            return response

        addressFromCheck = self.web3.toChecksumAddress(addressFrom)
        nonce = self.web3.eth.get_transaction_count(addressFromCheck)

        resp_ = self.trySendTx(net, amount, nonce, addressFrom,
                               addressTo, private, minerfee)

        if resp_['status'] == 'error':
            return resp_
        hashsend, fee_ = resp_['data']['hash'], resp_['data']['fee']

        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
            'HashSendClient': hashsend,
            'fee': fee_
        }
        return response
