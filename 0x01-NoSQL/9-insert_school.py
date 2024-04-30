#!/usr/bin/env python3
''' insert_school module '''


def insert_school(mongo_collection, **kwargs):
    ''' insert_school function '''
    return mongo_collection.insert_one(kwargs).inserted_id
