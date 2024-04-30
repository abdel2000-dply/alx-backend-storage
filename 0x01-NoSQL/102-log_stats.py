#!/usr/bin/env python3
''' Log stats '''
from pymongo import MongoClient


def log_stats():
    ''' Log stats '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    total = logs_collection.count_documents({})
    print("{} logs".format(total))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print("    method {}: {}".format(method, count))

    status_check = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))

    print("IPs:")
    top_ips = logs_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print("\t{}: {}".format(ip['_id'], ip['count']))


if __name__ == "__main__":
    log_stats()
