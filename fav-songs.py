from bson import ObjectId
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://shimaya_db_user:TRa4gg0IAttO1tLp@cluster0.ebvrcno.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGODB_URI)

db = client["music"]
collection = db["songs"]

app = Flask(__name__)

@app.route("/")
def start_index():
    return render_template("index.html")

@app.route("/list")
def song_list_page():
    #list of all songs
    return render_template("list.html")

#landing page for ap
@app.route("/welcome")
def welcome():
    return "<html><body><h1><em>Welcome to SoundKeep! Keep track of your favorite songs! </em></h1></body></html>"

#return a list of the songs 
@app.route("/songs",methods=["GET"]) 
def get_songs():
    songs = list(collection.find().sort("order", 1))
    for song in songs:
        song["_id"] = str(song["_id"])
    return jsonify(songs)

#add a new song to the collection
@app.route("/songs", methods=["POST"])
def add_song():
    new_song = request.get_json()
     #extract data 
    new_song = {
        "title": new_song.get("title"),
        "artist": new_song.get("artist")
    }
    #calc the order based on the current num of songs
    count = collection.count_documents({})
    new_song["order"] = count + 1
    
    collection.insert_one(new_song)
    return jsonify({"message": "Song added"}), 201

#remove a song from the list 
@app.route("/songs/<song_id>", methods=["DELETE"])
def delete_song(song_id):
    result = collection.delete_one({"_id": ObjectId(song_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "Song deleted!"}), 200
    else:
        return jsonify({"message": "Song not found!"}), 404


app.run(host = "0.0.0.0", port=3000)