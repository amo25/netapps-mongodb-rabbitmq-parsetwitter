import pymongo

stats = {"net": {"lo": {"rx": 0,"tx": 0},"wlan0":
                 {"rx": 708,"tx": 1192},"eth0": {"rx": 0,"tx":
                                                 0}},"cpu": 0.2771314211797171}
db = pymongo.MongoClient().test

db.utilization.insert(stats)