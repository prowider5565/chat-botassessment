import pymongo

mongo_client = pymongo.MongoClient(host="localhost", port=27017, tz_aware=True)

db = mongo_client["test_db"]
collection = db["users"]
mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"},
]

# x = collection.insert_many(mylist)
collection.delete_many({})

cln = collection.find()
# dict_values = [d.to_mongo() for d in cln]
print(list(cln))
