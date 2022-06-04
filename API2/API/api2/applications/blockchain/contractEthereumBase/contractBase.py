from web3 import Web3
from decimal import Decimal
from applications.cryptocurrencies.models import Cryptocurrencies
from applications.blockchain.contractEthereumBase.confContract import (
    ABI_USDTETH_TEST, ADDRESS_USDTETH_TEST,
    ABI_USDTETH_MAIN, ADDRESS_USDTETH_MAIN)
from applications.blockchain.contractEthereumBase.confContract import (
    ABI_SHIBAETH_TEST, ADDRESS_CONTRACT_SHIBAETH_TEST,
    ABI_SHIBAETH_MAIN, ADDRESS_CONTRACT_SHIBAETH_MAIN)
from applications.blockchain.contractEthereumBase.confContract import (
    ABI_USDCETH_TEST, ADDRESS_CONTRACT_USDCETH_TEST,
    ABI_USDCETH_MAIN, ADDRESS_CONTRACT_USDCETH_MAIN)
from applications.blockchain.contractEthereumBase.confContract import (
    ABI_TVKETH_TEST, ADDRESS_CONTRACT_TVKETH_TEST,
    ABI_TVKETH_MAIN, ADDRESS_CONTRACT_TVKETH_MAIN)
from applications.blockchain.contractEthereumBase.confContract import (
    ABI_HEXETH_TEST, ADDRESS_CONTRACT_HEXETH_TEST,
    ABI_HEXETH_MAIN, ADDRESS_CONTRACT_HEXETH_MAIN)


class contractBase:

    """
    Description:
    01 - Create class contractBase
    Author: Yessica Chuctaya
    Creation date : 2022
    Modification date: 06/04/2022
    """

    # PORT = 8545
    NODE_TEST = "https://ropsten.infura.io/v3/ff6b427c908e43beb64c2445c8eaf7e7"
    # NODE_MAIN = "https://mainnet.infura.io/v3/ff6b427c908e43beb64c2445c8eaf7e7"
    web3 = ''
    contract = ''

    def __init__(self, symbol, net):
        
        """
        Contructor of clase - indicates the ways to connect with the nodes
        """
        if net == "testnet" or net == "ropsten" or net == "rospten":
            self.web3 = Web3(Web3.HTTPProvider(self.NODE_TEST))
        else:
            self.web3 = Web3(Web3.HTTPProvider(self.NODE_MAIN))

        if self.web3.isConnected() is True:
            print('this a conect')
        else:
            print('It is not possible to establish a connection with the',
                  'Ethereum nodes')

        print('\n')
        # abi = json.loads(_abi)
        _abi, _addressSM, = self.switchSymbol(symbol, net)

        addressSM = self.web3.toChecksumAddress(_addressSM)
        self.contract = self.web3.eth.contract(address=addressSM, abi=_abi)

    def switchSymbol(self, symbol, net):
        
        """
        this function SwitchSymbol chooses which contract to enter:
        mainnet and testnet
        """
        
        if symbol == 'USDTETH':
            if net == 'testnet' or net == 'ropsten' or net == 'rospten':
                return ABI_USDTETH_TEST, ADDRESS_USDTETH_TEST
            else:
                return ABI_USDTETH_MAIN, ADDRESS_USDTETH_MAIN

        elif symbol == 'SHIBETH':
            if net == 'testnet' or net == 'ropsten' or net == 'rospten':
                return ABI_SHIBAETH_TEST, ADDRESS_CONTRACT_SHIBAETH_TEST
            else:
                return ABI_SHIBAETH_MAIN, ADDRESS_CONTRACT_SHIBAETH_MAIN

        elif symbol == 'USDCETH':
            if net == 'testnet' or net == 'rospten':
                return ABI_USDCETH_TEST, ADDRESS_CONTRACT_USDCETH_TEST
            else:
                return ABI_USDCETH_MAIN, ADDRESS_CONTRACT_USDCETH_MAIN

        elif symbol == 'TVKETH':
            if net == 'testnet' or net == 'rospten':
                return ABI_TVKETH_TEST, ADDRESS_CONTRACT_TVKETH_TEST
            else:
                return ABI_TVKETH_MAIN, ADDRESS_CONTRACT_TVKETH_MAIN

        elif symbol == 'HEXETH':
            if net == 'testnet' or net == 'rospten':
                return ABI_HEXETH_TEST, ADDRESS_CONTRACT_HEXETH_TEST
            else:
                return ABI_HEXETH_MAIN, ADDRESS_CONTRACT_HEXETH_MAIN

    def gasPriceCalculate(self, fee, gasLimit):
        """
        In case of changing the estimateGas variable, make the same change in
        api\scheduler\cryptocurrencies\bitcoin.py  function
        computeMinerFeeETHSM
        """
        
        if gasLimit == 0:
            estimateGas = 70000
        else:
            estimateGas = gasLimit

        gasPrice = fee/estimateGas
        return int(gasPrice * 10**18)

    def sendTx(self, net, amount, nonce,
               contract, addressFrom, addressTo,
               private, minerFee, web3, gasLimit):
            
        if net == "rospten" or net == "testnet":
            chainId = 3
        elif net == "mainnet":
            chainId = 1

        numDecimals = contract.functions.decimals().call()
        value = int(amount*(10**numDecimals))

        estimateGas = contract.functions.transfer(
            addressTo, value).estimateGas({'from': addressFrom})
        
        gasPrice = self.gasPriceCalculate(minerFee, gasLimit)
        
        maxPriorityFeePerGas = web3.toWei(2, 'gwei') 
        baseFeePerGas = web3.eth.get_block('pending')['baseFeePerGas']
        maxFeePerGas = (2 * baseFeePerGas) + maxPriorityFeePerGas
        maxFeePerGas = maxFeePerGas *10**(-18)

        txn = contract.functions.transfer(addressTo, value).buildTransaction({
            'chainId': chainId,
            'gas': estimateGas,
            'gasPrice': self.web3.toWei(maxFeePerGas, 'ether'),
            #'maxFeePerGas': self.web3.toWei(maxFeePerGas2, 'ether'),#web3.toWei('250', 'gwei'),
            #'maxPriorityFeePerGas':self.web3.toWei('2', 'gwei'),
            'nonce': nonce,
        })
        # SIGN IN
        privateKey = bytes.fromhex(private)
        signed = web3.eth.account.sign_transaction(txn, private_key=privateKey)
        try:
            tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)
        except Exception as e:
            print(e)
        hash_ = web3.toHex(tx_hash)
        result = self.web3.eth.get_transaction(hash_)
        fee = self.web3.fromWei(result['gasPrice'], 'ether') *  estimateGas

        return hash_, fee

    def trySendTx(self, net, amount, nonce,
                  contract, addressFrom, addressTo,
                  private, minerFee, web3, gasLimit):
        response = {
            'status': '',
            'message': '',
            'data': ''
        }

        nonceTrue = True
        count = 0
        while nonceTrue is True and count < 10:
            try:
                hash, fee = self.sendTx(
                    net, amount, nonce,
                    contract, addressFrom, addressTo,
                    private, minerFee, web3, gasLimit)
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

    def transaction(self, net, addressFrom, addressTo,
                    amount, addressCompany, gain,
                    private, minerfee, gasLimit):
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

        expenses = amount + gain
        availableAmount = self.contract.functions.balanceOf(addressFrom).call()
        numDecimals = self.contract.functions.decimals().call()
        availableAmount = Decimal(
            format(availableAmount/(10**numDecimals), ".8f"))

        if expenses > availableAmount:
            response['status'] = 'error'
            response['messages'] = 'insufficient balance token'
            return response

        amountEther = self.web3.eth.get_balance(addressFrom)
        if minerfee > amountEther:
            response['status'] = 'error'
            response['messages'] = 'insufficient ether'
            return response

        nonce = self.web3.eth.get_transaction_count(addressFrom)

        resp = self.trySendTx(net, amount, nonce, self.contract,
                              addressFrom, addressTo, private, minerfee,
                              self.web3, gasLimit)
        if resp['status'] == 'error':
            return resp
        hashsend = resp['data']['hash']
        nonce_, fee_send = resp['data']['nonce'], resp['data']['fee']

        resp_ = self.trySendTx(net, gain, nonce_ + 1, self.contract,
                               addressFrom, addressCompany, private,
                               minerfee, self.web3, gasLimit)
        if resp_['status'] == 'error':
            return resp_
        hashCompany, _, fee_company = resp_['data']['hash'], resp_[
            'data']['nonce'], resp_['data']['fee']

        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
            'HashSendCompany': hashCompany,
            'HashSendClient': hashsend,
            'fee': fee_send + fee_company
        }
        return response

    def importBase(self, net, addressFrom, addressTo,
                   amount, private, minerfee, gasLimit):
        response = {
            'status': '',
            'messages': '',
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

        availableAmount = self.contract.functions.balanceOf(addressFrom).call()
        numDecimals = self.contract.functions.decimals().call()
        availableAmount = Decimal(
            format(availableAmount/(10**numDecimals), ".8f"))
    
        if amount > availableAmount:
            response['status'] = 'error'
            response['messages'] = 'insufficient balance token'
            return response

        amountEther = self.web3.eth.get_balance(addressFrom)
        if minerfee > amountEther:
            response['status'] = 'error'
            response['messages'] = 'insufficient ether'
            return response

        nonce = self.web3.eth.get_transaction_count(
            self.web3.toChecksumAddress(addressFrom))

        resp_ = self.trySendTx(net, amount, nonce, self.contract,
                               addressFrom, addressTo, private, minerfee,
                               self.web3, gasLimit)
        if resp_['status'] == 'error':
            return resp_
        hashsend, _, fee_ = resp_['data']['hash'], resp_[
            'data']['nonce'], resp_['data']['fee']

        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
            'HashSendClient': hashsend,
            'fee': fee_
        }
        return response

    def exchange(self, net, addressFrom, addressTo,
                 amount, gain, private, minerfee, gasLimit):
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

        expenses = amount + gain
        availableAmount = self.contract.functions.balanceOf(addressFrom).call()
        numDecimals = self.contract.functions.decimals().call()
        availableAmount = Decimal(
            format(availableAmount/(10**numDecimals), ".8f"))

        if expenses > availableAmount:
            response['status'] = 'error'
            response['messages'] = 'insufficient balance token'
            return response

        amountEther = self.web3.eth.get_balance(addressFrom)
        if minerfee > amountEther:
            response['status'] = 'error'
            response['messages'] = 'insufficient ether'
            return response

        nonce = self.web3.eth.get_transaction_count(
            self.web3.toChecksumAddress(addressFrom))
        resp_ = self.trySendTx(net, amount, nonce, self.contract,
                               addressFrom, addressTo, private,
                               minerfee, self.web3, gasLimit)
        if resp_['status'] == 'error':
            return resp_
        hashsend, _, fee_ = resp_['data']['hash'], resp_[
            'data']['nonce'], resp_['data']['fee']

        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
            'HashSendClient': hashsend,
            'fee': fee_
        }
        return response
