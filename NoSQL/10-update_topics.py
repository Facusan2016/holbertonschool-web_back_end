#!/usr/bin/env python3
"""
    Python application to update a document.
"""


def update_topics(mongo_collection, name, topics):
    """Function to update a document"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
