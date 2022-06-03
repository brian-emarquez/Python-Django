# [Summary]
# This code is to create a transaction in tron node, is functional in testnet and
# mainnet with TRC10 token and TRC20.
# ------------------------
# Developed by: Ivan Cueva
# - email  : ivanedwin75@gmail.com
# - Date   : 10/02/2022
# - Update : 24/02/2022
###################################################################################

from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider

""" __Summary___
    This class is to set transactions in tron network, with TRC10 and TRC20 tokens.
    __Args______
    net: Determain if it is in mainnet or testnet
        mainnet     :   To do transactions with TRC10 tokens (TRX) in mainnet / with real money
        testnet     :   To do transactions with TRC10 tokens (TRX) in testnet / with fake tokens
        and you can use:
        #client = Tron(network="shasta")  # The Nile Testnet is preset or "shasta", "tronex", "nile"
        #client = Tron(HTTPProvider("http://127.0.0.1:8090"))  # Use private network as HTTP API endpoint
        #client = Tron()  # The default provider, mainnet
    cont: Determine what contract is using:
        "Tniknv..." :   Some contract / To do transactions with TRC20 tokens.
    __Returns___
    None
"""


class TronNetwork:
    impress = {}
    response = {}
    client = ''
    contract = ''

    def __init__(self, net, cont=0):

        self.impress = {
            "SUN": 0,
            "bandwidth": 0,
            "energy": 0,
            "amount_transfered": "",
            "wallet_amount_commission": "",
            "account_from_money_SUN": "",
            "transfer_ID": ""
        }
        # log: here is the log
        self.response = {
            'status': '',
            'messages': '',
            'data': ''
        }

        self.client = Tron() if net == 'mainnet' else Tron(network="nile")
        if type(cont) == str:  # If there's a contract as argument
            try:
                self.contract = self.client.get_contract(cont)
            except:
                self.response['messages'] = "Invalid Contract"
                self.response['status'] = 'Fail'

    """ __Summary___
        Validate an address, first search in the blockchain and then try to get the common qualities of an address in 
        this network.
        __Args______
        You have to pass a string
        __Returns___
        Return 0 if the string isn't a correct address, and return 1 if it's valid
    """

    def validateAddress(self, address):
        try:
            self.client.get_account(address)
            return 1
        except:
            if len(address) == 34 and address[0] == 'T':
                return 1
            else:
                self.response["status"] = "error"
                self.response["messages"] = "Invalid Address"
                return 0

    """ __Summary___
        It set the correct values in impress, to know how many resources
        are burning in a transaction.
        __Args______
        You have to pass the transaction ID, or hash
        __Returns___
        None
    """

    def calculate_fee_for_transaction(self, id_transaction):
        fee = self.client.get_transaction_info(id_transaction)
        if fee.get('fee') != None:
            self.impress['SUN'] += fee['fee']
        if fee.get('receipt').get('energy_usage') != None:
            self.impress['energy'] += fee['receipt']['energy_usage']
        if fee.get('receipt').get('net_usage') != None:
            self.impress['bandwidth'] += fee['receipt']['net_usage']

    """ __Summary___
        Check balance of an account, it means that determine how much money is in 
        the account.
        __Args______
        You have to pass a string / valid address
        __Returns___
        Return how much money there are in account, in SUN. You have to divide
        the result with 1000000 if you want in TRX.
    """

    def check_balance_SUN(self, address):
        balance = self.client.get_account_balance(address)
        return balance * 1000000

    """ __Summary___
        This function only is used when you do a transaction with TRC 20 tokens, with smarth contracts.
        Determine if user has the correct amount in TRX to pay fee in TRC20 tokens 
        __Args______
        You have to pass a string / valid address
        You have to pass an amount of fee in SUN
        __Returns___
        Return True or False
    """

    def check_Fee(self, address, fee):
        value = True if self.check_balance_SUN(address) > fee else False
        return value

    """ __Summary___
        Is a transaction build, and this function send the money.
        Build a transaction, it will be with smart contract or within it. 
        __Args______
        address_from        A valid address in the network
        priv_key            String of characteres in b58 decode
        address_to          Another valid address in the network
        amount              Amount in SUN
        note                Some message that you want to write in yor transaction
        __Returns___
        Return transaction ID/ hash of transaction.
    """

    def buildTRX(self, address_from, priv_key, address_to, amount, note):
        if self.contract == '':
            txn = (
                self.client.trx.transfer(address_from, address_to, amount)
                .memo(note)
                .build()
                .sign(priv_key)
            )
            return txn
        else:
            # If you use another contract decimals() will change
            amount = amount/1000000
            precision = self.contract.functions.decimals()
            amount = int(amount * 10 ** precision)
            ##########################
            txn = (
                self.contract.functions.transfer(address_to, amount)
                .with_owner(address_from)  # address of the private key
                .fee_limit(10_000_000)
                .build()
                .sign(priv_key)
            )
            return txn

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
        amount                      Amount that you want to send in SUN
        amount_commission           How many want to gain in commissions in SUN / = 0 (import)
        note                        Some message that you want to write in yor transaction
        minerFee                    minerfee amount in SUN
        __Returns___
        Return transaction ID/ hash of transaction of the main transaction (not of the commission).
    """

    def send_money_for_transaction(self, address_from, private_key, address_to, address_wallet, amount, amount_commission, note, minerFee):
        #(String, String, String, INT - sun, string)
        if self.validateAddress(address_from) and self.validateAddress(address_to):
            fee = True
            if self.contract == '':
                address_from_amount = self.check_balance_SUN(address_from)
            else:
                fee = self.check_Fee(address_from, minerFee)
                minerFee = 0
                address_from_amount = self.contract.functions.balanceOf(
                    address_from)

            if (amount + amount_commission + minerFee) > address_from_amount and not fee:
                self.response["status"] = "error"
                self.response["messages"] = "Error, amount is more than your actually money, please consider minery's amount too"
                return 0
            else:
                priv_key = PrivateKey(bytes.fromhex(private_key))

                # Only exec when transaction is an exchange
                exchange_commission = amount_commission if address_wallet == 'exchange' else 0
                # Exec only when is importing wallet
                txn = self.buildTRX(
                    address_from, priv_key, address_to, amount + exchange_commission, note)

                # Only exec when is standar transaction
                if address_wallet != '' and address_wallet != 'exchange' and amount_commission != 0:
                    txn_commission = self.buildTRX(
                        address_from, priv_key, address_wallet, amount_commission, note)
                    txn_commission.broadcast().wait()
                    self.calculate_fee_for_transaction(txn_commission.txid)

                txn.broadcast().wait()
                self.calculate_fee_for_transaction(txn.txid)

                self.impress['amount_transfered'] = amount
                self.impress['wallet_amount_commission'] = amount_commission
                self.impress['account_from_money_SUN'] = int(
                    address_from_amount - self.impress['amount_transfered'] - self.impress["SUN"] - self.impress['wallet_amount_commission'])
                # This must to be equal than address_from balance, if not something is wrong
                self.impress["transfer_ID"] = txn.txid
                return self.impress["transfer_ID"]
        else:
            return 0

    """ __Summary___
        The main function to defina client, and build all the logic.
        __Args______
        address_from                Sender's wallet address / string
        private_key                 Sender's private key with b58 encode
        address_to                  Receiver's wallet address / = address_wallet (if is exchange)
        address_wallet              Company wallet / Is 'exchange' if you want to do a exchange
        amount                      Amount that you want to send in SUN
        amount_commission           How many want to gain in commissions in SUN / = 0 (import)
        note                        Some message that you want to write in yor transaction
        minerFee                    minerfee amount in SUN
        __Returns___
        Return response, the correct minerfee, points of bandwidth burned, points of energy burned
    """

    def transactionTRX(self, address_from, private_key, address_to, address_wallet, amount, amount_commission, note, minerFee):
        transaction = self.send_money_for_transaction(
            address_from, private_key, address_to, address_wallet, amount, amount_commission, note, minerFee)
        if transaction != 0:
            self.response['status'] = 'Successful'
            self.response['data'] = self.impress['transfer_ID']
            minerFee = (int(self.impress["SUN"])) / 1000000
        else:
            self.response['status'] = 'error'
            self.response['messages'] = "Something is wrong!!"
        return self.response, minerFee, self.impress['bandwidth'], self.impress['energy']
