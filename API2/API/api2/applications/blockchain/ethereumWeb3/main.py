from decimal import Decimal

#from jsonrpcclient import requests
from createTransaction import createTransactionEth
from time import time

from re import I
import requests
import time

"""
    Description: Main
    to the network🚀
    Author: Brian Enrique Marquez Inca Roca
    Creation date: 2022
    Last modification: 04/04/2022
"""

#---------------------------- Gas Obsolete------------------------------------#
response = requests.get(f'https://ethgasstation.info/json/ethgasAPI.json')
gasPrice = response.json()['average']
gasPrice = int(gasPrice)
limitGas = 21000 * gasPrice
gas = limitGas
gasAumento = (gas * 10/100)
gas = gas + gasAumento
gas = gas * 0.00000000001
#-----------------------------------------------------------------------------#

data = {
    'addressOrigin': '0xa397aB58D260F94d7302FAa50cAdf741787043c7',
    'addressRecipient': '0x2BcdD2E4D29adD519d9958caa69c2abd86Aa05c0',
    'privateKey': '0e1b480d95e5524d9fea7b75fcd4504ca63b15564d84530015e45d39dbe36896',
    'walletCompany': '0x86a632C97920119c4b855f7De01d4244EdAa96d0',
    'net': "rospten",
    'amount': Decimal(f"{Decimal(0.9999000):.8f}"),
    'gain':  Decimal(f"{Decimal(0.0005800):.8f}"),
    #'gain':  Decimal(f"{Decimal(0.0000000):.8f}"),
    'minerFee': Decimal(f"{Decimal(gas):.8f}"),
    'recuperacion': False
}

#start_time = time()
response = createTransactionEth(data)
#elapsed_time = time() - start_time
#print("Elapsed time: %0.10f seconds." , elapsed_time)
print(response)
