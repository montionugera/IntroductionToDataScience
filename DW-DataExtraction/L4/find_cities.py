#!/usr/bin/env python
"""
Your task is to write a query that will return all cities
that are founded in 21st century.
Please modify only 'range_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""
from datetime import datetime


example_cities = {
    'areaCode': ['916'],
    'areaLand': 109271000.0,
    'country': 'United States',
    'elevation': 13.716,
    'foundingDate': datetime(2000, 7, 1, 0, 0),
    'governmentType': ['Council\u2013manager government'],
    'homepage': ['http://elkgrovecity.org/'],
    'isPartOf': ['California', u'Sacramento County California'],
    'lat': 38.4383,
    'leaderTitle': 'Chief Of Police',
    'lon': -121.382,
    'motto': 'Proud Heritage Bright Future',
    'name': 'City of Elk Grove',
    'population': 155937,
    'postalCode': '95624 95757 95758 95759',
    'timeZone': ['Pacific Time Zone'],
    'utcOffset': ['-7', '-8']
}
def range_query():
    # Modify the below line with your query.
    # You can use datetime(year, month, day) to specify date in the query
    query = {u'foundingDate' : {'$gte':datetime(2001, 1, 1, 0, 0)}}
    return query


# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db():
    from pymongo import MongoClient

    client = MongoClient('localhost:27017')
    db = client.examples
    return db


if __name__ == "__main__":
    # For local use
    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print "Found cities:", cities.count()
    import pprint

    pprint.pprint(cities[0])
