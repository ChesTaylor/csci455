from bigchaindb import Bigchain
import writeout
import random

b = Bigchain()

random.seed(3)

for x in range(1,8):
    # define a digital asset data payload
    digital_asset_payload = {'choice': random.randint(0,100)}

    # a create transaction uses the operation `CREATE` and has no inputs
    priv, pub = writeout.importData("user"+str(x))
    tx = b.create_transaction(b.me, pub, None, 'CREATE', payload=digital_asset_payload)
    #tx = b.create_transaction(b.me, pub, None, 'CREATE')


    # all transactions need to be signed by the user creating the transaction
    tx_signed = b.sign_transaction(tx, b.me_private)
    writeout.exportData(tx_signed, "user"+str(x)+"vote")

    # write the transaction to the bigchain
    # the transaction will be stored in a backlog where it will be validated,
    # included in a block, and written to the bigchain
    print(b.write_transaction(tx_signed))


