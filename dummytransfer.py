from bigchaindb import Bigchain
import writeout

b = Bigchain()

govt_priv, govt_pub = writeout.importData("govt")

for x in range(1,8):
    priv, pub = writeout.importData("user"+str(x))
    tx_signed = writeout.importData("user"+str(x)+"vote")
    tx_retrieved = b.get_transaction(tx_signed['id'])
    print(tx_retrieved)


    # create a transfer transaction
    tx_transfer = b.create_transaction(pub, govt_pub, tx_retrieved['id'], 'TRANSFER')
    print(tx_transfer)

    # sign the transaction
    tx_transfer_signed = b.sign_transaction(tx_transfer, priv)
    print(tx_transfer_signed)

    # write the transaction
    b.write_transaction(tx_transfer_signed)

    # check if the transaction is already in the bigchain
    tx_transfer_retrieved = b.get_transaction(tx_transfer_signed['id'])

    print(tx_transfer_retrieved)

    data = b.validate_transaction(tx_transfer_signed)
    print(data)
