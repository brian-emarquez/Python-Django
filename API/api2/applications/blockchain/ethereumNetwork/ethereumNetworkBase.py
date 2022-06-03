from web3 import Web3

class ERC20NetworkBase:

    """
    Author: Yessica Chuctaya
    Modification date: 11/03/2022
    Description: 
        01 - Create class ERC20NetworkBase
    """
    
    node_url= "" # Red Testnet
    chainId = ""
    url_explorer = "" 

    web3 = ""
     
    #def __init__(self, url_main, chainId_main, explorer_main, url_test, chainId_test, explorer_test,work):
    def __init__(self, url, chainId, explorer):
        self.node_url = url
        self.chainId = chainId
        self.url_explorer = explorer

        self.web3 = Web3(Web3.HTTPProvider(self.node_url))

        if self.web3.isConnected() == True:
            print('  Conect url node    ')
        else:
            print('  Failed conect      ')
        print('\n')
        
    def calculateMaxFeePerGas(self):
        maxPriorityFeePerGas = self.web3.toWei(2, 'gwei')
        baseFeePerGas = 2*self.web3.toWei(self.web3.eth.get_block('pending')['baseFeePerGas'], 'gwei') 
        maxFeePerGas = baseFeePerGas + maxPriorityFeePerGas
        gasPrice = maxFeePerGas - maxPriorityFeePerGas

        return maxFeePerGas,gasPrice

    def sendTx(self, net, amount, nonce, addressFrom, addressTo, private, minerFee):
        
        gas = self.web3.eth.estimate_gas({'to': addressTo, 
                                          'from':addressFrom, 
                                          'value': self.web3.toWei(amount, 'ether')})
        print('gas  :', gas)
        #maxFeePerGas =  minerFee/gas
        try:
            baseFeePerGas = self.web3.eth.get_block('pending')['baseFeePerGas']
            print('.........baseFeePerGas ', baseFeePerGas)
        except Exception as e:
            print('error', e,'\n')

        

        tx = {
            'nonce' : nonce,
            'chainId': self.chainId,
            #'gasPrice' :gasPrice,
            'gas':  gas, 
            'to': addressTo,
            'value' : self.web3.toWei(amount, 'ether'),    
            'maxFeePerGas': self.web3.toWei('25', 'gwei'),# self.web3.toWei(minerFee, 'wei'), #self.web3.toWei(maxFeePerGas, 'ether'),# maxFeePerGas,#self.web3.toWei(minerFee, 'wei'),
            'maxPriorityFeePerGas': self.web3.toWei('2', 'gwei'),
        }
        print(tx)
        #SIGN IN
        try:
            signed = self.web3.eth.account.sign_transaction(tx, private)
        except Exception as e:
            print('error', e,'\n')

        #SEND TRX
        try:
            tx_hash = self.web3.eth.send_raw_transaction(signed.rawTransaction) 
        except Exception as e:
            print('error', e,'\n')

        hash_ = self.web3.toHex(tx_hash)
        result = self.web3.eth.get_transaction(hash_)
        fee = self.web3.fromWei(result['gasPrice'], 'ether') * gas
    
        return hash_,fee

    def trySendTx(self,net, amount, nonce, addressFrom,addressTo, private, minerFee):
        response = {
            'status':'',
            'message':'',
            'data':''
        }
        nonceTrue = True
        count = 0
        while nonceTrue == True and count< 2:
            try:
                hash,fee = self.sendTx(net, amount, nonce,addressFrom, addressTo, private, minerFee)
                nonceTrue = False
                response['status'] ='successful'
                response['data']={
                    'hash':hash,
                    'nonce':nonce,
                    'fee':fee
                }
            except:
                response['status']='error'
                response['message']='transaction failed'
                nonce +=1
                count +=1

        return response

    def transaction(self,net,addressFrom, addressTo, amount, addressCompany, gain, private, minerfee):
        response = {
            'status':'',
            'message':'',
            'data':''
        }

        if self.web3.isAddress(addressFrom) == False:
            response['status']='error'
            response['messages']='The origin address is not valid'
            return response
        
        if self.web3.isAddress(addressTo) == False:
            response['status']='error'
            response['messages']='The destination ad dress is not valid'
            return response
        
        if self.web3.isAddress(addressCompany) == False:
            response['status']='error'
            response['messages']='The company wallet address is not valid'
            return response
        
        expenses = amount + gain + minerfee
        expenses = self.web3.toWei(expenses, 'ether') 
        availableAmount = self.web3.eth.get_balance(addressFrom)

        if expenses > availableAmount:
            response['status']='error'
            response['messages']='insufficient balance token' 
            return response
        
        nonce = self.web3.eth.get_transaction_count(addressFrom)

        print('----->',(net, amount, nonce, addressFrom, addressTo, private, minerfee))
        resp =  self.trySendTx(net, amount, nonce, addressFrom, addressTo, private, minerfee)
        if resp['status']=='error':
            return resp
        hashsend,nonce_, fee_send = resp['data']['hash'],resp['data']['nonce'], resp['data']['fee']

        resp_ =  self.trySendTx(net, gain, nonce_ + 1,addressFrom, addressCompany, private, minerfee)
        if resp_['status']=='error':
            return resp_
        hashCompany,_, fee_company = resp_['data']['hash'],resp_['data']['nonce'], resp_['data']['fee']

        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
                    'HashSendCompany':hashCompany,
                    'HashSendClient':hashsend ,
                    'fee' :fee_send + fee_company
            }
        return response

    def importBase(self,net, addressFrom, addressTo, amount, private,minerfee):
        response = {
            'status':'',
            'message':'',
            'data':''
        }
        if self.web3.isAddress(addressFrom) == False:
            response['status']='error'
            response['messages']='The origin address is not valid'
            return response
        
        if self.web3.isAddress(addressTo) == False:
            response['status']='error'
            response['messages']='The destination ad dress is not valid'
            return response

        expenses = amount +  minerfee
        expenses = self.web3.toWei(expenses, 'ether') 
        availableAmount = self.web3.eth.get_balance(addressFrom)

        if expenses > availableAmount:
            response['status']='error'
            response['messages']='insufficient balance ' 
            return response
        
        nonce = self.web3.eth.get_transaction_count(self.web3.toChecksumAddress(addressFrom)) 
 
        resp_ =  self.trySendTx(net, amount, nonce,  addressFrom, addressTo, private, minerfee)
        if resp_['status']=='error':
            return resp_
        hashsend,_ , fee_ = resp_['data']['hash'],resp_['data']['nonce'], resp_['data']['fee']


        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
            'HashSendClient':hashsend,
            'fee':fee_
        }  
        return response
        
    def exchange(self, net, addressFrom, addressTo, amount, gain, private,minerfee):
        response = {
            'status':'',
            'message':'',
            'data':''
        }
        if self.web3.isAddress(addressFrom) == False:
            response['status']='error'
            response['messages']='The origin address is not valid'
            return response
        
        if self.web3.isAddress(addressTo) == False:
            response['status']='error'
            response['messages']='The destination ad dress is not valid'
            return response

        expenses = amount + gain + minerfee
        expenses = self.web3.toWei(expenses, 'ether') 
        availableAmount = self.web3.eth.get_balance(addressFrom)
        
        if expenses > availableAmount:
            response['status']='error'
            response['messages']='insufficient balance ' 
            return response
        
        nonce = self.web3.eth.get_transaction_count(self.web3.toChecksumAddress(addressFrom)) 
        resp_ =  self.trySendTx(net, amount, nonce, addressFrom, addressTo, private, minerfee)       
        if resp_['status']=='error':
            return resp_
        hashsend,_ , fee_ = resp_['data']['hash'],resp_['data']['nonce'], resp_['data']['fee']
        
        response['status'] = 'successful'
        response['messages'] = 'transaction sent'

        response['data'] = {
                        'HashSendClient':hashsend ,
                        'fee':fee_
                        }
        return response

        
        