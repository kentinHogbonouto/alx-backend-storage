#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score
"""
import pymongo


def top_students(mongo_collection):
    """
    Python function that returns all students sorted by average score
    Args:
        mongo_collection: collection to be queried
    Return:
        All students sorted by average score
    """
    # Establishing connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    sorted_students = mongo_collection.aggregate([
        {'$project': {'averageScore': {'$avg': "$topics.score"},
                      'name': 1, 'topics': 1}},
        {'$sort': {'averageScore': -1}}
        ])
    return sorted_students
