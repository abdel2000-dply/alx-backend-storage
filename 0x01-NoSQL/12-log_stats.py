#!/usr/bin/env python3
"""
script that provides some stats about
Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def log_stats():
    """
    Nginx logs stored in MongoDB
    """
    client = MongoClient('localhost', 27017)
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    count_status = collection.count_documents({"method": "GET",
                                                    "path": "/status"})
    print(f"{count_status} status check")


if __name__ == "__main__":
    log_stats()
