#!/usr/bin/env python3
""" python function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """ update_topics.
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
