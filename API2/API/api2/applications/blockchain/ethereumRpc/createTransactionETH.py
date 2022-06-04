import decimal
from pprint import pprint
from decimal import Decimal
from ethrpc import jsrpc
from .listunspentUTXOETH import listunspentUTXOETH

def preCalculation_InputsOuputs(rpc,txInfo, extraInfo):
    
    response = {
            'status':'',
            'message':''
    }
   
    #Validate Addressess
    if rpc.validateaddress(txInfo['addressOrigin'])['isvalid'] == False:
        response['status'] = 'error'
        response['message'] = 'AddressOrigin  invalid'
        return response

    if rpc.validateaddress(txInfo['addressRecipient'])['isvalid'] == False:
        response['status'] = 'error'
        response['message'] = 'AddressRecipient invalid'
        return response
    
    if extraInfo['companyAddressWallet']:
        if rpc.validateaddress(extraInfo['companyAddressWallet'])['isvalid'] == False:
            response['status'] = 'error'
            response['message'] = 'companyAddressWallet invalid'
            return response
    
    if extraInfo['minerFee'] <=0:
        response['status'] = 'error'
        response['message'] = 'Miner fee cannot be 0 or lest'
        return response

    #Inputs and ouputs
    expenses = txInfo['amount'] + extraInfo['gain'] + extraInfo['gasPrice']
    #expenses = txInfo['amount'] + extraInfo['gain'] + extraInfo['minerFee']
    
    #---------------------------------------------------------------------------------------------#
    utxos = listunspentUTXOETH(rpc,txInfo['addressOrigin'],extraInfo['net'],expenses)#'addressOrigin'
    
    if not utxos:
        response['status'] = 'error'
        response['message'] = 'Not enough to spend'
        return response

    if type(utxos)==tuple:
        utxos = utxos[0]

    inputs = []
    outputs = []

    # INPUTS 
  
    amount_available = 0
    for utxo in utxos:
        if utxo:
            inputs.append({
                        "txid": utxo['txid'],
                        "vout": utxo['vout']
            })
            amount_available += utxo['amount']

    #OUPUTS
    addresses = []
    addresses.append((txInfo['addressRecipient'],txInfo['amount'])) #DESTINO
    
    if extraInfo['companyAddressWallet']:
        addresses.append((extraInfo['companyAddressWallet'],extraInfo['gain'])) #addrescompany 

    if amount_available - expenses > 0.0001: 
        addresses.append((txInfo['addressOrigin'],amount_available - expenses)) #origin(vuelto) address_origin
    else:
        extraInfo['minerFee'] += amount_available - expenses 
    
    addresses_oupts = dict()
    for address,amount in addresses:
        if not address in addresses_oupts :
            addresses_oupts[address]  =  amount
        else:
            addresses_oupts[address] += amount #Decimal(f"{amount:.8f}")

    #[{"txid": "2feac07b9fd6f64bad6f61f2bef953d3fd14bc7831e3830c4a3b214211ffe46c", "vout": 1}]
    #[{"mkqYWeQbtmHeEGoTJaktXGbbkNf5GKZV3H": Decimal("0.00998977")}]
    for address in addresses_oupts:
        outputs.append({address:float(f"{addresses_oupts[address]:.8f}")})
    
    response['status']='successful'
    response['message']='correct !'
    response['data']={
        'inputs':inputs,
        'outputs':outputs,
        'utxos':utxos,
        'amountAvailable':amount_available
    }
    return response

"""
def createTransactionETH(rpc,txInfo, extraInfo):

    response = {
            'status':'',
            'message':''
    }
    #CALCULATION INPUTS - OUPUTS
    respIO = preCalculation_InputsOuputs(rpc,txInfo,extraInfo)

    if respIO['status']=='error':
        return respIO

    inputs = respIO['data']['inputs']
    outputs = respIO['data']['outputs']
  
    #CREATERAWTRANSACTION
    #print('\n')
    #print('createTX  -> ',inputs,'  ',outputs)

    try:
        tx_hex=  rpc.createrawtransaction(inputs,outputs)
    except:
        response['status'] = 'error'
        response['message'] = 'Error in createrawtransaction'
        return response
        
    response['status'] = 'successful'
    response['message'] = 'Createrawtransaction '
    response['data'] = respIO['data']
    response['data']['tx_hex'] = tx_hex
    
    return response"""
    
