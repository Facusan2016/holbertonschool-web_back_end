#!/usr/bin/env python3
"""
    Python application to list all documents.
"""


def list_all(mongo_collection):
    """Function to list all documents"""
    docs = mongo_collection.find()
    if not docs:
        return []
    return docs
