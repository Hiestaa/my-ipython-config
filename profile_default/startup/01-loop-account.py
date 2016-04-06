# -*- coding: utf8 -*-

try:
    from server import cachedRequestsService as CRS

    def getAccountId(accountName):
        accounts = CRS.retrieveAccounts()
        for accId, acc in accounts.iteritems():
            if acc['uname'] == accountName:
                return accId
        raise Exception("Account %s does not exist" % accountName)
except Exception as e:
    def getAccountId(accountName):
        raise Exception("Unable to load `cachedRequestsService` module from "
                        "`server` package. Are you in the NLP repository?")
    print("Error while executing: 01-loop-account.py")
else:
    print("")
    print("Executed: 01-loop-account.py")
    print("")
