from rpc import Rpc

NODE_URL_TEST = "http://127.0.0.1:8370"
NODE_USER_TEST = 'bitcoin'
NODE_PASSWORD_TEST = '2*C@;fEv1PWOxwy'

NODE_URL_TEST_LOCAL = "http://127.0.0.1:18370"
NODE_USER_TEST_LOCAL = 'user'
NODE_PASSWORD_TEST_LOCAL = 'password'


class Syscoin:
    """
    Author: Yessica Chuctaya
    Modification date: 03/03/2022
    Description: 
    01 - Create class Syscoin
    """
    rpc = ''

    def __init__(self):
        self.rpc = Rpc(
            NODE_URL_TEST_LOCAL, 
            NODE_USER_TEST_LOCAL, 
            NODE_PASSWORD_TEST_LOCAL)
        
        result = self.rpc.getnetworkinfo()
        if result['result']:
            print('   Syscoin node is conect ')
        else:
            print('   Syscoin node is not conect ')
    
    def validateAddress(self, address):
        result = self.rpc.validateaddress(address)
        return result['result']['isvalid']

    def transaction(self, net, addressFrom, addressTo, 
                    amount, addressCompany, gain, private, 
                    minerfee):
        response = {
            'status': '',
            'message': '',
            'data': ''
        }

        if not self.validateAddress(addressFrom):
            response['status'] = 'error'
            response['message'] = 'The origin address is not valid'
            return response

        if not self.validateAddress(addressTo):
            response['status']='error'
            response['message']='The destination address is not valid'
            return response
        
        if not self.validateAddress(addressCompany):
            response['status']='error'
            response['message']='The company wallet address is not valid'
            return response

        expenses = amount + gain + minerfee
        
        utxos = self.rpc.listunspent()

        return response