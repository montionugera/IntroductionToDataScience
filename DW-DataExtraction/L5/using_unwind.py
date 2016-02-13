#!/usr/bin/env python
"""
For this exercise, let's return to our cities infobox dataset. The question we would like you to answer
is as follows:  Which region or district in India contains the most cities?

As a starting point, use the solution for the example question we looked at -- "Who includes the most
user mentions in their tweets?"

One thing to note about the cities data is that the "isPartOf" field contains an array of regions or 
districts in which a given city is found. See the example document in Instructor Comments below.

"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
                {"$match": {"name" : {"$exists":1},"country":"India"}},
                {"$unwind":"$isPartOf"},
                {"$group":{"_id":"$isPartOf","count":{"$sum":1}}},
                #{"$match": {"_id" :"Uttar Pradesh"}},
                 {"$sort": {"count":-1} },
                 {"$limit": 1} ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    print "Printing the first result:"
    import pprint
    pprint.pprint(result[0])
    assert result[0]["_id"] == "Uttar Pradesh"
    assert result[0]["count"] == 623


