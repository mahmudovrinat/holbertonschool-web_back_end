#!/usr/bin/env python3
"""Insert a document in a Python"""

def insert_school(mongo_collection, **kwargs):
    """Insert a document to a MongoDB collection"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
