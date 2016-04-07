import hashlib
# monkey patch hashlib with sha3 functions
import sha3
import json

from bigchaindb import Bigchain
import writeout

b = Bigchain()


user1priv, user1pub = writeout.importData("user1")
user2priv, user2pub = writeout.importData("user2")
user3priv, user3pub = writeout.importData("user3")
govt_priv, govt_pub = writeout.importData("govt")


gids = b.get_owned_ids(govt_pub)

for id in gids:
    t = b.get_transaction(id)
    print(t)

#data = {'vote': 30}
#tx_serialized = bytes(json.dumps(data, skipkeys=False, ensure_ascii=False, separators=(',', ':')).encode("utf-8"))
#tx_hash = hashlib.sha3_256(tx_serialized).hexdigest()
#txs = b.get_tx_by_payload_hash(tx_hash)
#for tx in txs:
#    print(tx)

