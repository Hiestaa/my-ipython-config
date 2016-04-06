# -*- coding: utf8 -*-
from IPython.core.magic import register_line_magic

mongo = None
db = None
client = None


class DB(object):
    """Wrapper to access to some mongo database"""
    def __init__(self, client):
        super(DB, self).__init__()
        self.client = client
        self.dbName = 'test'
        self.db = self.client[self.dbName]

    def use(self, dbName):
        print("Switching to db %s" % dbName)
        self.db = self.client[dbName]

    def showCollections(self):
        print('\n'.join(self.db.collection_names()))

    def dropDatabase(self):
        self.client.drop_database(self.dbName)

    def __getattr__(self, collection):
        return self.db[collection]


@register_line_magic
def use(dbName):
    db.use(dbName)


@register_line_magic
def show(dataType):
    if dataType in ['dbs', 'databases']:
        print('\n'.join(client.database_names()))
    elif dataType == 'collections':
        db.showCollections()
    else:
        print("Unknown item: %s" % dataType)

try:
    from server import distributed
    mongo = distributed.findService('mongo')
    if not mongo:
        raise Exception(
            "Unable to find mongoDB server URL - defaulting to "
            "localhost running instance.")
except Exception as e:
    print("WARNING: 02-mongo-attempt: " + str(e))
    mongo = {'address': 'localhost', 'port': '27017'}

try:
    from pymongo import MongoClient
    client = MongoClient(mongo['address'], mongo['port'])
    db = DB(client)
except Exception as e:
    print("Error while executing: 02-mongo-attempt.")
    raise e
else:
    print("")
    print("Connected to database: test")
    print("You should know have a `db` global object to interract with mongoDB"
          " server in a similar way it is done in the mongo shell:")
    print("")
    print(">>> db.use('nlp_dev') # use('nlp_dev') works as well.")
    print("Switching to db nlp_dev")
    print(">>> db.nlp_loops.findOne()")
    print("{...}")
    print(">>> db.showCollections()")
    print("auto_response")
    print("custom_filter")
    print("...")
    print("Executed: 02-mongo-attempt.")
    print("")
