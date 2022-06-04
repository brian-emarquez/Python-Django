import os
import json
PATH_ = os.path.dirname(os.path.abspath(__file__))
DIRNAME_ = 'abi'


def readJson(filename):
    with open(os.path.join(PATH_, DIRNAME_, filename)) as json_file:
        data = json.load(json_file)
    return data


# TETHER Ethereum
ABI_USDTETH_TEST = readJson('abi_usdt_eth_testnet.json')
ADDRESS_USDTETH_TEST = '0xFFf4FB1b7f768f97Ef7c5d52428C393140Fd1b6E'

ABI_USDTETH_MAIN = readJson('abi_usdt_eth.json')
ADDRESS_USDTETH_MAIN = '0xdAC17F958D2ee523a2206206994597C13D831ec7'

# SHIBA INU Ethereum
ABI_SHIBAETH_TEST = readJson('abi_shibainu_eth_testnet.json')
ADDRESS_CONTRACT_SHIBAETH_TEST = '0xcF1AF2D88A9D2C4c3752fb5FdeA133F15969d7F3'

ABI_SHIBAETH_MAIN = readJson('abi_shibainu_eth.json')
ADDRESS_CONTRACT_SHIBAETH_MAIN = '0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE'

# USD COIN Ethereum
ABI_USDCETH_TEST = readJson('abi_usdt_eth_testnet.json')
ADDRESS_CONTRACT_USDCETH_TEST = '0xF82324094efe8903E471D995fC64389147Fb0F63'

ABI_USDCETH_MAIN = readJson('abi_usdc_eth.json')
ADDRESS_CONTRACT_USDCETH_MAIN = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'

# Terra Virtua Ethereum
ABI_TVKETH_TEST = readJson('abi_tvk_eth_testnet.json')
ADDRESS_CONTRACT_TVKETH_TEST = '0xa2cfe6E4d621f18c22B47873A29ec8c466372E6f'

ABI_TVKETH_MAIN = readJson('abi_tvk_eth.json')
ADDRESS_CONTRACT_TVKETH_MAIN = '0xd084B83C305daFD76AE3E1b4E1F1fe2eCcCb3988'

# HEX Ethereum
ABI_HEXETH_TEST = readJson('abi_hex_eth.json')
ADDRESS_CONTRACT_HEXETH_TEST = '0xB2112A3eda2EA035d89F224F290A8Ff7B28B4c7e'

ABI_HEXETH_MAIN = readJson('abi_hex_eth_testnet.json')
ADDRESS_CONTRACT_HEXETH_MAIN = '0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39'
