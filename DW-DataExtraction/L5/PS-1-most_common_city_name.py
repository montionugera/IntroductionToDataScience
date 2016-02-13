__author__ = 'montionugera'
# !/usr/bin/env python
"""
Use an aggregation query to answer the following question.

What is the most common city name in our cities collection?

Your first attempt probably identified None as the most frequently occurring city name.
What that actually means is that there are a number of cities without a name field at all.
It's strange that such documents would exist in this collection and, depending on your situation,
might actually warrant further cleaning.

To solve this problem the right way, we should really ignore cities that don't have a name specified.
As a hint ask yourself what pipeline operator allows us to simply filter input?
How do we test for the existence of a field?



"""


def get_db(db_name):
    from pymongo import MongoClient

    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def make_pipeline():
    # complete the aggregation pipeline

    # What is the most common city name in our cities collection?

    # pipeline = [
    #             {"$match": {"name" : {"$exists":1}}},
    #             {"$group":{"_id":"$name","count":{"$sum":1}}},
    #              {"$sort": {"count":-1} },
    #              {"$limit": 1}
    #             ]

    # Which Region in India has the largest number of cities with longitude between 75 and 80?
    # pipeline = [
    #     {"$match": {"lon": {"$gte": 75, "$lte": 80}, "country": "India"}},
    #     {"$unwind": "$isPartOf"},
    #     {"$group": {"_id": "$isPartOf", "count": {"$sum": 1}}},
    #     {"$sort": {"count": -1}},
    #     {"$limit": 1}
    # ]

    # find the average regional city population
    # for all countries in the cities collection. What we are asking here is that you first calculate the
    # average city population for each region in a country and then calculate the average of all the
    # regional averages for a country.
    pipeline = [
                {"$unwind":"$isPartOf"},
                {"$group":{"_id":{"region":"$isPartOf","country":"$country",},"avg":{"$avg":"$population"}}},
                {"$group":{"_id":"$_id.country","avgRegionalPopulation":{"$avg":"$avg"}}},
    ]
    return pipeline


def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    # The following statements will be used to test your code by the grader.
    # Any modifications to the code past this point will not be reflected by
    # the Test Run.
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint

    pprint.pprint(result[0])
    assert len(result) == 1
    assert result[0] == {'_id': 'Shahpur', 'count': 6}
