#!/usr/bin/env python3
"""
    Python application to update a document.
"""


def schools_by_topic(mongo_collection, topic):
    """Function to update a document"""
    docs = mongo_collection.find({"topics": topic})
    if not docs:
        return []
    return docs
