#!/usr/bin/env python3
"""Lists all documents in a MondoDB clloection"""

def list_all(mongo_collection):
    """Lists all documents in a collection"""
    documents = list(mongo_collection.find())
    return documents
