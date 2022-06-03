from web3 import Web3


"""
    Title:   Infura Hosted Node Backup 🚀
    Made by: Brian Enrique Marquez Inca Roca
    Email:   9780desarrollador07@gmail.com
    Date:    9/02/2022
"""


def web3EthInfura(net):
    """
    Nodo alojado Ethereum (Infura)
    """

    NODE_Test = "https://ropsten.infura.io/v3/67bdc7c7edd14ba8af0f15d262fb38b8"
    NODE_Main = "https://mainnet.infura.io/v3/67bdc7c7edd14ba8af0f15d262fb38b8"

    """
    # Nodo alojado Ethereum (Moralis)
    NODE_URL_INFURA =
    "https://speedy-nodes-nyc.moralis.io/02fcbc458e4dc52b0021c579/eth/ropsten"
    """

    if net == 'ropsten' or net == 'testnet':
        web3node = Web3(Web3.HTTPProvider(NODE_Test))
    else:
        web3node = Web3(Web3.HTTPProvider(NODE_Main))

        """ We test the connection with the Ethereum node """

        if(web3node.isConnected() is True):
            print("Success : successful connection to node Infura")
            print("test infura", web3node.eth.block_number)
            return web3node

        else:
            print("Error: Cannot establish Infura connection")
            return ""
