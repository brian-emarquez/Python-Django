# [Summary]
# Create a transaction in solana network, is functional in testnet and
# mainnet.
# ------------------------
# Created by: Jose Fuentes (01/02/2022)
# - email  : 9780desarrollador13@gmail.com
# Checked by: Ivan Cueva
# - email  : ivanedwin75@gmail.com
# - Update : 16/03/2022
###################################################################################
 
from solana.keypair import Keypair
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
import base58 as bs58
""" __Summary___
    Validate an address, first search in the blockchain and then try to
    get the common qualities of an address in this network.
    __Args______
    You have to pass a string
    __Returns___
    Return 0 if the string isn't a correct address, and return 1 if it's valid
"""


def validateAddress(address):
    if (client.get_account_info(address)):
        return 1
    else:
        if len(address) == 44:
            return 1
        else:
            self.response["status"] = "error"
            self.response["messages"] = "Invalid Address"
            return 0


""" __Summary___
    Check balance of an account, it means that determine how much money is in 
    the account.
    __Args______
    You have to pass a string / valid address
    __Returns___
    Return how much money there are in account, in lamports. You have to divide
    the result with 1000000000 if you want in SOL.
"""


def checkBalance(address):
    balance = client.get_balance(address)
    return int(balance['result']['value'])


""" __Summary___
    Is a transaction build, and this function send the money.
    __Args______
    address_from        A valid address in the network
    priv_key            String of characteres in b58 decode
    address_to          Another valid address in the network
    amount              Amount in lamports
    skip_confirmation   True, if you want to skip, or false if you want to wait
    __Returns___
    Return transaction ID/ hash of transaction.
"""


def buildSOL(address_from, priv_key, address_to, amount, skip_confirmation):
    txn = Transaction().add(transfer(TransferParams(
        from_pubkey=address_from,
        to_pubkey=address_to,
        lamports=int(amount))))
    txn_block = client.send_transaction(
        txn, priv_key, opts=TxOpts(skip_confirmation=skip_confirmation))
    return txn_block['result']


""" __Summary___
    Is a function where you have to consolidate the correct information depend 
    that you want to do (transaction / exchange / import).
    (my_wallet,         my_pk, another_wallet,  company_wallet,  amount,            amount_commission,      minerFee) transaction
    (my_wallet,         my_pk, company_wallet,  'exchange',      amount,            minerfeeX + minerfeeY,  minerFee) exchange
    (my_another_wallet, my_pk, my_wallet,       '',    balance(my_wallet)-minerfee, 0,                      minerFee) importation
    __Args______
    address_from                Sender's wallet address / string
    private_key                 Sender's private key with b58 encode
    address_to                  Receiver's wallet address / = address_wallet (if is exchange)
    address_wallet              Company wallet / Is 'exchange' if you want to do a exchange
    amount                      Amount that you want to send in lamports
    amount_commission           How many want to gain in commissions in lamports / = 0 (import)
    minerFee                    minerfee amount in lamports
    __Returns___
    Return transaction ID/ hash of transaction of the main transaction (not of the commission).
"""


def send_money_for_transaction(address_from, private_key, address_to, address_wallet, amount, amount_commission, minerFee):
    if validateAddress(address_from) and validateAddress(address_to):
        address_from_amount = checkBalance(address_from)
        if (amount + amount_commission + minerFee) >= address_from_amount:
            response["status"] = "error"
            response["messages"] = "Error, amount is more than your actually money, please consider minery's amount too"
            return 0
        else:
            priv_key = Keypair.from_secret_key(bs58.b58decode(private_key))

            # Only exec when transaction is an exchange
            exchange_commission = amount_commission if address_wallet == 'exchange' else 0
            # Only exec when is standar transaction
            if address_wallet != '' and address_wallet != 'exchange' and amount_commission != 0:
                txn_commission = buildSOL(
                    address_from, priv_key, address_wallet, amount_commission, True)

            # Exec only this, when is a wallet importation
            txn = buildSOL(address_from, priv_key, address_to,
                           amount + exchange_commission, False)

            return txn
    else:
        return 0


""" __Summary___
    The main function to defina client, and build all the logic.
    __Args______
    address_from                Sender's wallet address / string
    private_key                 Sender's private key with b58 encode
    address_to                  Receiver's wallet address / = address_wallet (if is exchange)
    address_wallet              Company wallet / Is 'exchange' if you want to do a exchange
    amount                      Amount that you want to send in lamports
    amount_commission           How many want to gain in commissions in lamports / = 0 (import)
    minerFee                    minerfee amount in lamports
    net                         it could be mainnet or testnet
    __Returns___
    Return response.
"""


def transactionSOL(address_from, private_key, address_to, address_wallet, amount, amount_commission, minerFee, net):
    global client, response
    response = {
        'status': '',
        'messages': '',
        'data': ''
    }

    client = Client("https://api.mainnet-beta.solana.com") if net == 'mainnet' else Client(
        "https://api.devnet.solana.com")

    transaction = send_money_for_transaction(
        address_from, private_key, address_to,
        address_wallet, amount, amount_commission, minerFee)
    
    if transaction != 0:
        response['status'] = 'Successful'
        response['data'] = transaction
    else:
        response['status'] = 'error'
        response['messages'] = "Something is wrong!!"

    return response
