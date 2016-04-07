You must run these files on a computer with both rethinkdb & bigchaindb installed and running

1. dummyusers.py creates users and saves their keypairs
2. dummyvote.py creates "vote" data for each user and writes it to the db
3. checkvote.py checks if each users "vote" has been written to the db
4. dummytransfer.py transfers each users "vote" to the "govt" user
5. checkinventory.py checks all of the transactions owned by the "govt" user

**Client->Server API:**

Global commands:
* login_request (creds::Credential)

Voter commands:
* vote_request (ARGS GO HERE)
* check_vote_request (ARGS GO HERE)

Administrator commands:
* assign_votes (ARGS GO HERE)
* ??
* profit

**Server->Client API:**

Global commands:
* login_response (ARGS GO HERE)

Voter commands:
* vote_response (ARGS)
* check_vote_response (ARGS)

Administrator commands:
* i don't even know
