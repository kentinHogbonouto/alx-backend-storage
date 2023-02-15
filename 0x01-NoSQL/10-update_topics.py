#!/usr/bin/env python3
"""
Python function that updates a documents topic based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Python function that updates a documents topic based on the name
    Args:
        mongo_collection: collection to be queried
        name: name of document to be updated
        topics: updated topics
    Return:
        Updated documents
    """
    # Establishing connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
