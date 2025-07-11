#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

def log_stats(mongo_collection):
    """Prints log stats from a MongoDB collection."""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_count = mongo_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_count} status check")

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    log_stats(client.logs.nginx)
