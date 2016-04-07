from bigchaindb import Bigchain
import json

b = Bigchain()

def exportData(data, filename):
    f = open(filename, 'w')
    f.write(b.serialize(data))
    #json.dump(data, f)

def importData(filename):
    f = open(filename, 'r')
    return b.deserialize(f.read())
