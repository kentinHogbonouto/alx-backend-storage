#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    Python function that lists all documents in a collection
    Args:
        mongo_collection: collection to be queried
    Return:
        List of all documents in a collection
        An empty list is returned if no document is in the collection
    """
    # Establishing connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return [doc for doc in mongo_collection.find()]
