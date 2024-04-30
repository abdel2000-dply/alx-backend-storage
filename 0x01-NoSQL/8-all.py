#!/usr/bin/env python3
''' list all documents in a collection '''


def list_all(mongo_collection):
    ''' list all '''
    return list(mongo_collection.find())
