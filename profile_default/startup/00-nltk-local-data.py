# -*- coding: utf8 -*-
test = 'test'
try:
    import nltk
    nltk.data.path.append('nltk_data')
except Exception as e:
    print("Error while executing: 00-nltk-local-data.py")
    raise e
else:
    print("")
    print("Executed: 00-nltk-local-data.py")
    print("")
