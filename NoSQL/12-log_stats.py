#!/usr/bin/env python3
"""
    Python application to update a document.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    """Main program"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.logs.nginx
    print(f'{col.count_documents({})} logs')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')
    for met in methods:
        print(f'\tmethod {met}: {col.count_documents({"method": met})}')
    print(f'{col.count_documents({"method": "GET", "path": "/status"})}'
          ' status check')
