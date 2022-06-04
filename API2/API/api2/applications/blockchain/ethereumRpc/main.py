import pprint
#from rest_framework.fields import EmailField
#from web3 import Web3, providers
import json
from decimal import Decimal
from ethrpc import jsrpc
import ast
from pprint import pprint

def sendTxETH(addressOrigin,
              addressRecipient,
              amount,
              gas,
              gasPrice, 
              private_key,
              #net
):
    
    """ transacion sendTxETH 
    ref: https://eth.wiki/json-rpc/API#eth_sendrawtransaction """
    
    nonce = rpc.eth_getTransactionCount(addressOrigin, "latest")
            
    """if net == "rospten":
        chainId = 3
    elif net == "mainnet":
        chainId = 1"""
            
    params = {
        #'chainId': net,
        'nonce' : nonce,
        'from':addressOrigin,
        'to' : addressRecipient,
        'value': "0x9184e72a", 
        #'value' : ethereumConnect.toWei(str(amount), 'wei'),  
        'gas': "0x76c0", 
        #'gasPrice': ethereumConnect.toWei('50', 'gwei' )  
        'gasPrice': "0x9184e72a000" 
        #'gasPrice': ethereumConnect.toWei(str(gasPrice), 'wei' ),
    }
    """print('\n')
    pprint(params)"""
    
    print(params)
    #s = ast.literal_eval(s)
    #print(s)
       
    signTx = rpc.eth_signTransaction(params)
    print(signTx)
    
    """hashTx = rpc.eth_sendRawTransaction(params)
    print("send", hashTx)"""

    #Firma
    """signed_tx = ethereumConnect.eth.account.signTransaction(tx, private_key)
    tx_hash = ethereumConnect.eth.sendRawTransaction(signed_tx.rawTransaction)
    
    print(ethereumConnect.toHex(tx_hash))      
    return ethereumConnect.toHex(tx_hash)""" 

# ------------------------------ create trasaction ----------------------------------
def createTransactionEth(addressOrigin,
                         addressRecipient, 
                         walletCompany,
                         private_key, 
                         amount, gain, 
                         gas, 
                         gasPrice 
                         #net
):
    #print(ethereumConnect.isConnected())
    """
    Method to createrawwtransactions to ETH 
    """
    
    response = {
        'status':'',
        'messages':'' 
    }
        # Validate Address    
    #result = Web3.isAddress(addressOrigin)
    #print("validador ", result)
    
    """activate, rpc = jsrpc()
    if  rpc.isAddress(addressOrigin) == False:
        response['status']='error'
        response['messages']='The origin address is not valid'
        print('The origin address is not valid')
        return response
    
    if Web3.isAddress(addressRecipient) == False:
        response['status']='error'
        response['messages']='The destination address is not valid'
        print('The destination address is not valid')
        return response"""
    
    hassendCompany = ''
    hassend = sendTxETH(addressOrigin, 
                        addressRecipient,
                        amount,
                        gas, 
                        gasPrice, 
                        private_key 
                        #net
                        )
    
    if gain != 0 and walletCompany != '':
        
        """if Web3.isAddress(walletCompany) == False:
            response['status']='error'
            response['messages']='The destination walletCompany is not valid'
            print('The destination address is not valid')
            return response"""
        
        #time.sleep(25)
        #print("hassend", hassend)
        #if hassend:
        hassendCompany = sendTxETH(addressOrigin, 
                                   walletCompany,
                                   gain,
                                   gas,
                                   gasPrice,
                                   private_key
                                   #net
                                   )
        response['status'] = 'successful'
    response['messages'] = 'transaction sent'
    response['data'] = {
        'hassendCompany':hassendCompany,
        'hassend':hassend 
    }
    
    return response  
    totalAmount = amount + gain + gasPrice + gasPrice 

#------------------------------------- MAIN ----------------------------------------

addressOrigin = "0xc468aff54d7638b1a5e5ea1c027db215b3a201de"
addressRecipient = "0xa397aB58D260F94d7302FAa50cAdf741787043c7"
#addressRecipient = "0x5dc2388093d504b603F88696de439180DdE1e108"
private_key = "85f7cc8cefe2dd90765634a71845bc65e21a488a543b1eacc6a66bcd9850d3a6"
#private_key = "ab6167091b974bebeb25177ba68a98864429f330f356d9945a436663d574c58b"
walletCompany = "0x2BcdD2E4D29adD519d9958caa69c2abd86Aa05c0"
#net = "rospten"
#walletCompany = ""
#amount = "0x9184e72a"
amount = hex(int(Decimal(1.000000)))
#amount = int(f"{Decimal(1.500000):.8f}")
gain = Decimal(f"{Decimal(0.500000):.8f}")
#gain = Decimal(f"{Decimal(0.000000):.8f}")

activate, rpc = jsrpc()
block = ast.literal_eval(rpc.eth_blockNumber())
#block = ast.literal_eval(block)

#gasPrice =  "0x9184e72a000"
gasPrice =  "0x9184e72a000"
#limitGas = "0x76c0"
#limitGas = 2100
gas = "0x76c0"
#gas = gasPrice * limitGas

print('.....:ETHEREUM:......') 
 
# pprint(params)
# sendTransactionraw(addressOrigin,addressRecipient)
response = createTransactionEth(addressOrigin,
                                addressRecipient,
                                walletCompany,
                                private_key,
                                amount,
                                gain,
                                gas,
                                gasPrice
                                #net
                                )
if response['status'] == 'error':
    print(response['message'])
else:
    print(response)
    

"""print("---------------TEST-ETHEREUM------------------")
print(hassend)
#print(hassendCompany)
print(totalAmount)
print('aquiii')"""