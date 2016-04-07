from bigchaindb import Bigchain
import writeout

b = Bigchain()


for x in range(1,4):
    tx_signed = writeout.importData("user"+str(x)+"vote")
    tx_retrieved = b.get_transaction(tx_signed['id'])
    print(b.transaction_exists(tx_retrieved['id']))

