#!/usr/bin/env python3
""" python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """ insert_school.
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
