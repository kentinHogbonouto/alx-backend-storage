#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in
MonogDB
"""
import pymongo


if __name__ == "__main__":
    # Establishing connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Getting db
    db = client["logs"]

    # Collection name
    col = db["nginx"]

    print(f"{col.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {col.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {col.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {col.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {col.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {col.count_documents({'method': 'DELETE'})}")
    print("{} status check".
          format(col.count_documents({'method': 'GET', 'path': '/status'})))
