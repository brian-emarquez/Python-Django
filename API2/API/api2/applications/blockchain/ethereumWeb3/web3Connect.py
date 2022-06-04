from web3 import Web3
from .web3Infura import web3EthInfura

"""
    Description:
    Connection to Ethereum node 🚀
    Author: Brian Enrique Marquez Inca Roca
    Creation date : 2022
    Last modification_ 06/04/2022
"""


def web3EthConnect(net):
    """
    We test the connection with the Ethereum node
    """

    # PORT = 8545
    NODE_Test = "https://ropsten.infura.io/v3/67bdc7c7edd14ba8af0f15d262fb38b8"
    NODE_Main = "https://mainnet.infura.io/v3/67bdc7c7edd14ba8af0f15d262fb38b8"

    if net == 'rospten' or net == 'testnet' or 'ropsten':
        web3node = Web3(Web3.HTTPProvider(NODE_Test))
    else:
        web3node = Web3(Web3.HTTPProvider(NODE_Main))

    response = {}
    response['status'] = ''
    response['message'] = ''

    if(web3node.isConnected() is True):
        print("Success : successful connection to node 9780 Eth ")
        response['status'] = 'successful'
        response['message'] = 'connection to node 9780 Eth'
        response['web3node'] = web3node

        return response

    else:
        responseResp = web3EthInfura(net)
        if responseResp:
            response['status'] = 'successful'
            response['message'] = 'connection to node Infura'
            response['web3node'] = responseResp
            return response
        else:
            response['status'] = 'Error'
            response['message'] = 'It is not possible to establish a ',
            'connection with the Ethereum'
            response['web3node'] = responseResp
            return response
