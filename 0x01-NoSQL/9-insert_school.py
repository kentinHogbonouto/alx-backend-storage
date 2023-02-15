#!/usr/bin/env python3
"""
Python function that inserts a document into a collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts a document into a collection
    Args:
        mongo_collection: collection to be queried
        kwargs: document to be inserted
    Return:
        Id of inserted document
    """
    # Establishing connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    id = mongo_collection.insert_one(kwargs).inserted_id
    return id
