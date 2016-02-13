import os

__author__ = 'montionugera'
import json

current_path = os.path.dirname(os.path.realpath(__file__))

DATAFILE = os.path.join(current_path, 'arachnid.json')
def insert_data(data, db):

    # Your code here. Insert the data into a collection 'arachnid'

    db.arachnid.insert(data)


if __name__ == "__main__":

    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open(DATAFILE) as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()