
from pprint import pprint
from decimal import Decimal
#from cryptos import Litecoin
import math

"""def listUnspent(net,address):  
    if net == 'testnet':
        c = Litecoin(testnet=True)
    elif net == 'mainnet':
        c = Litecoin(mainnet=True)
    
    if c:
        inputs = c.unspent(address)
        
    result = []
    conversor = Decimal(0.000000001)
    if inputs:
        for input in inputs:
            output = input['output']
            value = input['value'] # esta en Litoshi
            idx_c = output.find(':')
            result.append({
                 'txid': output[:idx_c],
                 'vout': int(output[idx_c + 1:]),
                 'amount': Decimal(f"{value*conversor:.8f}")
            })
    return result"""

def listunspentUTXOETH(rpc,address,net,target):
    listunspend = rpc.listunspent() #0,10,["Qi6H3VffzHckaSXkqLaAYhbFkKYQ74m3Mh"]
    list_unspent = []
    
    for unspent in listunspend:
        if unspent['address']==address:
            list_unspent.append(unspent)

    if len(list_unspent)<=0:
        list_unspent = listUnspent(net,address)
    #print('list_unspent')
    #print(list_unspent)
    utxo = coinSelectionNew(list_unspent,target)#coinSelection(list_unspent,target)
    
    return utxo
def coinSelection(utxos, target):
    """
    Method to obtain the best set of utxos fro testnet
    """
    lower_utxos = []
    lower_values = []

    greater_utxo = []
    greater_value = math.inf

    for idx, tx in enumerate(utxos):
        if tx['amount']==target:
            return [tx]
        if tx['amount']<target:
            lower_values.append( tx['amount'] )
            lower_utxos.append( ([tx], tx['amount'], 0) )
        elif tx['amount'] < greater_value:
            greater_utxo= [tx]
            greater_value = tx['amount']
        if len(utxos)-1==idx:
            if sum(lower_values) == target:
                return lower_utxos
            elif greater_utxo:
                return greater_utxo
            else:
                inputs = ()
                r,i = combinatorial(lower_utxos, target, inputs)
                #print('> r ', r)
                #print()
                return i
    return []
def coinSelectionNew(utxos, target):
    """
    Method to obtain the best set of utxos fro mainnet
    utxo sortedy descending
    """

    bestset = []
    sum = 0
    smallCoins = []
    maxGreater = []

    utxos.sort(key=lambda x: x['amount'],reverse=True)
    
    for utxo in utxos:
        #MatchSingleCheck
        if utxo['amount']==target:
            bestset = [utxo]
            return bestset
        #SumOfSmallerChecks
        if utxo['amount']<target:
            sum += utxo['amount']
            smallCoins.append(utxo)
        #Calculate greater 
        if  utxo['amount']>target:
            maxGreater = [utxo]
   
    if sum==target:
        return smallCoins
    elif maxGreater:
        return maxGreater
    elif sum>target:
        #ordenar de forma ascendiente
        bestset_ = []
        sum_ = 0
        for utx in smallCoins:
            sum_ += utx['amount']
            bestset_.append(utx)
            if sum_ >= target:
                return bestset_
    else:
        return []

def combinatorial(utxos, target, inputs):
    """
    Method to get the opimals utxos
    utxos: Transactions retrieve from the blockchain
    target: Amount of bitcoin to be spent (should be in satoshis)
    inputs: List to append utxos optimals
    """
    if len(utxos)==0:
        return [([''],0,0)], inputs 
    r , w = combinatorial(utxos[:-1], target, inputs)
    #print('>w :', w)
    temp = []  
    if w and w[2]==3:
        pass
    else:
        for s in r:
            actual=utxos[-1]
            aux_0=s[0] + actual[0]
            aux_1=s[1] + actual[1]
            aux=(aux_0, aux_1, len(aux_0))
            if aux[1]>=target:
                if w:
                    if aux[2]<=w[2]:
                        w=aux
                else: 
                    w=aux
            temp.append(aux)
    r=r + temp
    return r, w

