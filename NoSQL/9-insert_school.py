#!/usr/bin/env python3
"""
    Python application to insert a document.
"""


def insert_school(mongo_collection, **kwargs):
    """Function to insert a document"""
    new_obj = mongo_collection.insert_one(kwargs)
    return new_obj.inserted_id
