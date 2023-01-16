#!/usr/bin/env python3
""" python function that lists all documents in a collection
"""

import pymongo


def list_all(mongo_collection):
    """ list_all.
    """
    docs = mongo_collection.find()
    return [x for x in docs]
