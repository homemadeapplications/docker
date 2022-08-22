import os
from pymongo import MongoClient

def start_chuck_db(uri: str):
    client = get_client(uri)
    db = client.chuck_db
    return db

def get_client(uri: str) -> MongoClient:
    return MongoClient(uri)

def add_blague(db, blague):
    db.blagues.insert_one(blague)
    print("insertion element OK")

def create_blague():
    return {
        'titre': 'pouet',
        'description': 'pouet pouet'
    }

if __name__ == "__main__":
    print ("lancement du programme de blague a chuck norris")
    match os.environ.get("DB_CHUCK_NORRIS"):
        case str() as uri:
            print (f"lancement de la db avec l'uri : {uri}")
            db = start_chuck_db(uri)
            add_blague(db, create_blague())
        case None:
            print ("No db uri found on environments variables")
        case _: 
            print ("Error")