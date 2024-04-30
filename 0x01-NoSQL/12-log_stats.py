#!/usr/bin/env python3
''' Log stats '''
from pymongo import MongoClient


def log_stats():
    ''' Log stats '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    total = logs_collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_check = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
