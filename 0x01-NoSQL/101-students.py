#!/usr/bin/env python3
''' top_students Module '''


def top_students(mongo_collection):
    ''' top_students function '''
    return mongo_collection.aggregate([
        { "$unwind": "$topics" },
        { "$group": { "_id": "$name", "averageScore": { "$avg": "$topics.score" } } },
        { "$sort": { "averageScore": -1 } }
    ])
