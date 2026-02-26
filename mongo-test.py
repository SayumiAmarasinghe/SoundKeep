from pymongo import MongoClient
MONGODB_URI = "mongodb+srv://shimaya_db_user:TRa4gg0IAttO1tLp@cluster0.ebvrcno.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGODB_URI)

db = client["music"]
collection = db["songs"]

""""
#insert one doc
collection.insert_one({"title": "Almost Love", "artist": "Sabrina Carpenter", "order": 1})
collection.insert_one({"title": "Calgary", "artist": "Tate McRae"})
collection.insert_one({"title": "People Watching", "artist": "Conan Gray"})
#read (find one doc)
"""


for f in collection.find():
    print(f)