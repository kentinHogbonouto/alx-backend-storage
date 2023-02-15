#!/usr/bin/env python3
"""
Python function that returns the list of schools
having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Python function that returns the list of schools
    having a specific topic
    Args:
        mongo_collection: collection to be queried
        topics: updated topics
    Return:
        List of Schools that contain the topic
    """
    # Establishing connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    schools = mongo_collection.find({'topics': {'$regex': topic}})
    return schools
