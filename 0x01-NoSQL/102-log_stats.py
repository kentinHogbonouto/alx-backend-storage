#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in
MonogDB, includes the top 10 of the most present IPs in the collection
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

    top10Ips = db.nginx.aggregate([
        {'$group': {
            '_id': "$ip",
            'ip_count': {'$sum': 1}
        }},
        {'$sort': {'ip_count': -1}},
        {'$limit': 10}
    ])

    print("IPs:")
    for ip in top10Ips:
        print(f"\t{ip.get('_id')}: {ip.get('ip_count')}")
