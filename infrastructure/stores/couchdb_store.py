from cloudant.client import CouchDB


class CouchDBStore:

    def __init__(self):
        user = "admin"
        password = "password"
        self.couchserver = CouchDB(user, password, url='http://127.0.0.1:5984', connect=True)
        self.couchserver.session()

    def create_db(self, db):
        self.couchserver.create_database(db)

    def get_all_db(self):
        return [dbname for dbname in self.couchserver]

    def append(self, db, data):
        self.couchserver[db].create_document(data)

    def close(self):
        self.couchserver.disconnect()




import time
import uuid

event = {
    "root_id": "c8ce3e13-07bb-4479-9e2a-a28900822722",
    "type": "ResearchGroup.",
    "name": "RG 1",
    "timestamp": time.time(),
}

# 56e2a06e-85e6-4b97-aad7-7ec9cb40421d

x = CouchDBStore()
#x.create_db("events")

x.append("events", event)
print(event)

x.couchserver.disconnect()




