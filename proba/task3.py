from pymongo import MongoClient
from bson.json_util import loads
from pprint import pprint


client = MongoClient()
db = client.test_database
accounts = db.accounts

with open("Account.bson") as f:
        new_accounts = loads(f.read())

result = accounts.insert_many(new_accounts)
print(result.inserted_ids)

# TODO Suppress output _id field with $project

pipeline = [
    {"$unwind": "$sessions"},
    {"$unwind": "$sessions.actions"},
    {"$group": {"_id": {"number": "$number", "action": "$sessions.actions.type"},
                "created_at": {"$push": "$sessions.actions.created_at"},
                "count": {"$sum": 1}}},
    {"$group": {"_id": {"number": "$_id.number"},
                "actions": {"$push": {"type": "$_id.action", "last": {"$max": "$created_at"}, "count": "$count"}}}}
]

pprint(list(accounts.aggregate(pipeline)))