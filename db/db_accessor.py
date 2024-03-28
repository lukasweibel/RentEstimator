import os
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)
    
db = client['mdm']
    
rent_collection = db['rent']

model_collection = db['model']



def add_entry_to_db(rent, area, rooms, zip_code):
    document = {
        'rent': rent,
        'area': area,
        'rooms': rooms,
        'zip': zip_code
    }

    if rent_collection.find_one(document) is None:
        rent_collection.insert_one(document)
        print("Entry added to database.")
    else:
        print("Document already exists. Skipping insertion.")


def delete_all_entries():
    rent_collection.delete_many({})
    print("All documents deleted.")

def get_all_entries():
    documents = rent_collection.find({})
    documents_list = list(documents)
    cleaned_data = [{k: v for k, v in d.items() if k != '_id'} for d in documents_list]
    df = pd.DataFrame(cleaned_data)
    return df

def add_model(r_squared, entries_number, name):
    document = {
        "r-squared": r_squared,
        "entries": entries_number,
        "name": name
    }
    result = model_collection.insert_one(document)
    print(f"Inserted document with ID: {result.inserted_id}")

def get_all_models():
    documents = model_collection.find({})
    documents_list = list(documents)
    return documents_list


    