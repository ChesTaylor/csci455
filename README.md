You must run these files on a computer with both rethinkdb & bigchaindb installed and running

1. dummyusers.py creates users and saves their keypairs
2. dummyvote.py creates "vote" data for each user and writes it to the db
3. checkvote.py checks if each users "vote" has been written to the db
4. dummytransfer.py transfers each users "vote" to the "govt" user
5. checkinventory.py checks all of the transactions owned by the "govt" user

**Operations:**

Admin:
* Create election
* Assign votes during election

Voter:
* Vote
* Check vote
* Check election status?
