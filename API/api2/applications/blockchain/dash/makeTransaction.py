from cryptos import *
dash = Dash(testnet=True)
#tx = dash.preparesignedtx(priv, 
#                          "Xhcmzs5wKECBiWwSEsTZu8wNonguH5poaz", 
#                          9800000-20000, 
#                          fee=20000)
#dash.send("89d8d898b95addf569b458fbbd25620e9c9b19c9f730d5d60102abbabcb72678", "yd8Q7MwTDe9yJdeMx1YSSYS4wdxQ2HDqTg", 1200000000)
#{'status': 'success', 'data': {'txid': '6a510a129bf1e229e99c3eede516d3bde8bdccf859199937a98eaab2ce1cd7ab', 'network': 'DASHTEST'}}

addr1 = 'yQVSL2NiBCCFeaD2nX2uRAby6EfoYrsrzF'
addr2 = 'yckZatvsG3w31W4Qq1DwmqjA1uZYMyGfHa'

"""
import sys
from pycoin.symbols.tdash import network
from pycoin.tx.tx_utils import *

def write_transfer(sender, sender_priv, recipient, message, fee=m.default_fee, avoid_inputs=[]):
    message = hexlify(message.encode()).decode('utf8')
    print(message)
    spendables = spendables_for_address(sender)
    spendables = [s for s in spendables if not spendable_to_legible(s.tx_in()) in avoid_inputs]
    bitcoin_sum = sum([spendable.coin_value for spendable in spendables])
    inputs = [spendable.tx_in() for spendable in spendables]
    outputs = []
    if bitcoin_sum > fee + m.dust*2:
        remaining = bitcoin_sum - fee - m.dust*2
        dest_output_script = standard_tx_out_script(recipient)
        change_output_script = standard_tx_out_script(sender)
        btc_change_output_script = standard_tx_out_script(sender)
        op_return_output_script = script.tools.compile("OP_RETURN %s" % message)

        outputs.append(TxOut(m.dust, dest_output_script))
        outputs.append(TxOut(m.dust, change_output_script))
        outputs.append(TxOut(remaining, btc_change_output_script))
        outputs.append(TxOut(0, op_return_output_script))

        tx = Tx(version=1, txs_in=inputs, txs_out=outputs)
        tx.set_unspents(spendables)
        sign_tx(tx, wifs=[sender_priv])
        print(tx.as_hex())
        return tx.as_hex()
    else:
        print("INADEcUATE FUNDS")

addr1 = 'yQVSL2NiBCCFeaD2nX2uRAby6EfoYrsrzF'
addr2 = 'yckZatvsG3w31W4Qq1DwmqjA1uZYMyGfHa'

print(spendable_to_legible(s.tx_in(addr1)))
        

def externalfunction():
    if len(sys.argv) != 4:
        print("usage: %s incoming_tx_hex_filename tx_out_index new_address" % sys.argv[0])
        sys.exit(-1)

    with open(sys.argv[1], "r") as f:
        tx_hex = f.readline().strip()

    # get the spendable from the prior transaction
    tx = network.tx.from_hex(tx_hex)
    tx_out_index = int(sys.argv[2])
    spendable = tx.tx_outs_as_spendable()[tx_out_index]

    # make sure the address is valid
    payable = sys.argv[3]
    assert network.parse.address(payable) is not None

    # create the unsigned transaction
    tx = network.tx_utils.create_tx([spendable], [payable])

    print("here is the transaction: %s" % tx.as_hex(include_unspents=True))


if __name__ == '__main__':
    main()
    
"""
"""import sys

from pycoin.encoding.hexbytes import h2b
from pycoin.symbols.btc import network


def main():
    if len(sys.argv) != 4:
        print("usage: %s tx-hex-file-path wif-file-path p2sh-file-path" % sys.argv[0])
        sys.exit(-1)

    # get the tx
    with open(sys.argv[1], "r") as f:
        tx_hex = f.readline().strip()
    tx = network.tx.from_hex(tx_hex)

    # get the WIF
    with open(sys.argv[2], "r") as f:
        wif = f.readline().strip()
    assert network.parse.wif(wif) is not None

    # create the p2sh_lookup
    with open(sys.argv[3], "r") as f:
        p2sh_script_hex = f.readline().strip()
    p2sh_script = h2b(p2sh_script_hex)

    # build a dictionary of script hashes to scripts
    p2sh_lookup = network.tx.solve.build_p2sh_lookup([p2sh_script])

    # sign the transaction with the given WIF
    network.tx_utils.sign_tx(tx, wifs=[wif], p2sh_lookup=p2sh_lookup)

    bad_solution_count = tx.bad_solution_count()
    print("tx %s now has %d bad solution(s)" % (tx.id(), bad_solution_count))

    include_unspents = (bad_solution_count > 0)
    print("Here is the tx as hex:\n%s" % tx.as_hex(include_unspents=include_unspents))


if __name__ == '__main__':
    main()
    """