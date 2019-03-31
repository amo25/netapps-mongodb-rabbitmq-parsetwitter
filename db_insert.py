import pymongo
import json
import time
#
#insert_json = {"net": {"lo": {"rx": 0,"tx": 0},"wlan0":
                 #{"rx": 708,"tx": 1192},"eth0": {"rx": 0,"tx":
                                                 #0}},"cpu": 0.2771314211797171}
#db = pymongo.MongoClient().test

#db.utilization.insert(stats)

#todo pull in as args
Action = "p"
Place = "Squires"
Subject = "Rooms"
Message = "I like the comfortable chairs"

ticks = time.time()
MsgID = "19" + "$" + str(ticks)

insert_json = {
    "Action": Action,
    "Place": Place,
    "MsgID": MsgID,
    "Subject": Subject,
    'Message': Message
    }
#insert_json = json.dumps(insert_json)
#print(insert_json)

client = pymongo.MongoClient()
db = client[Place]
collection = db[Subject]
collection.insert_one(insert_json)