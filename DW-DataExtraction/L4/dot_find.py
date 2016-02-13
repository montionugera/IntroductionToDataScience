#!/usr/bin/env python
"""
Your task is to write a query that will return all cars with width dimension
greater than 2.5. Please modify only the 'dot_query' function, as only that
will be taken into account.
"""
# width dimension greater than 2.5
# {
# 	"_id" : ObjectId("52fd438b5a98d65507d288cf"),
# 	"engine" : "Crawler-transporter__1",
# 	"dimensions" : {
# 		"width" : 34.7472,
# 		"length" : 39.9288,
# 		"weight" : 2721000
# 	},
# 	"transmission" : "16 traction motors powered by four  generators",
# 	"modelYears" : [ ],
# 	"productionYears" : [ ],
# 	"manufacturer" : "Marion Power Shovel Company",
# 	"name" : "Crawler-transporter"
# }

def dot_query():
    # Edit the line below with your query - try to use dot notation.
    # You can check out example_auto.txt for an example of the document
    # structure in the collection.
    query = {"dimensions.width": {"$gt": 2.5}}
    return query


# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db():
    from pymongo import MongoClient

    client = MongoClient('localhost:27017')
    db = client.examples
    return db


if __name__ == "__main__":
    db = get_db()
    query = dot_query()
    cars = db.cars.find(query)

    print "Printing first 3 results\n"
    import pprint

    for car in cars[:3]:
        pprint.pprint(car)
