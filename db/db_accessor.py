import os
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)
    
db = client['mdm']
    
collection = db['rent']

def add_entry_to_db(rent, area, rooms, zip_code):
    document = {
        'rent': rent,
        'area': area,
        'rooms': rooms,
        'zip': zip_code
    }

    if collection.find_one(document) is None:
        collection.insert_one(document)
        print("Entry added to database.")
    else:
        print("Document already exists. Skipping insertion.")


def delete_all_entries():
    collection.delete_many({})
    print("All documents deleted.")

def get_all_entries():
    documents = collection.find({})
    documents_list = list(documents)
    cleaned_data = [{k: v for k, v in d.items() if k != '_id'} for d in documents_list]

    df = pd.DataFrame(cleaned_data)
    return df