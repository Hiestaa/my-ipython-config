# my-ipython-config

This is the ipython configuration I use in my dev environment.
This repo is designed to enable me (or anyone interested in trying this config) to define and keep habits, shortcuts and other handy utilities to be used during my devs and be sure I'll never have to do it again.

## Disclaimer

This config is very specific to my work. Some features might not work for you, or may seem to be irrelevant. Please ignore them - you might enjoy some others.
You don't have to keep this README: the list of features will be described in the ipython header on start-up.

## Setting up

### Profile

To install this config in your own version of ipython, follow these simple steps:

* Run `git clone git@github.com:Hiestaa/my-ipython-config.git` to retrieve the configuration files, or download and extract the zip archive of this repo.
* If you haven't done it already, run `ipython profile create` to create a default profile. I imagine you might want to create another profile for my config if you've created the default one already.
* Copy the content of `profile_default` into your ipython profile. If you just created the default one, simply run the following command: `cp -r profile_default ~/.ipython/`

Now, run the ipython binary. You should see the following output (or similar):


### Extensions

TODO

## Features List

This ipython configuration currently holds the following features:

### Automatic Import

The following packages from the standard library are automatically imported on start-up:
```python
sys, os, re, json, base64, calendar, csv, datetime, itertools, functools, random, hashlib, tempfile, argparse, math, random, subprocess, uuid4 (from uuid), datetime, timedelta (from datetime), Counter, OrderedDict, defaultdict (from collections)
```

Moreover, the following features from python3 are imported on start-up as well:
```python
unicode_literals, absolute_import, division (from __future__)
```

Finally, if any of the following external lib is available, it will be loaded as well:

```python
path (from path), dateutil, relativedelta (from dateutil), requests, pymongo, nltk
```

### NLTK Local Data

If you're using NLTK (Natural Language ToolKit), and you want to keep NLTK data in the local folder of your project, NLTK will fail to retrieve its data unless you add the `./nltk_data` to the NLTK data path.

This is done automatically if NLTK can be be imported.

### MongoDB

If you're using MongoDB, you might or might not like the mongo shell, but you most certainly like (joke inside) the python driver.
To avoid the cumbersome of creating a `MongoClient` connected to the local instance of the MongoDB server, this is automatically done as well when starting up ipython. As a result, you will have access to a `db` global object that can be used in a similar way it is used in the mongo shell. The following commands are available:

```python
db.use('database')  # switch to the database given by name
db.showCollections()  # show the list of collection registered for the current database
db.dropDatabase()  # drop the current database
db.myCol.fn()  # execute "fn" method of "myCol" collection on the current database.
```

A few magic methods can also come handy:

```python
%use database  # switch current db to 'database'
%show collections  # show the list of available collections for the current database
%show dbs; %show databases  # show the list of available databases on the server.
```

This is where the similarity with mongo shell stops though. Database calls will return python objects, and the interface will be the one defined by pymongo.