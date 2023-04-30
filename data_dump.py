import pymongo  
import pandas as pd
import json

'''
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://LNarayan:<password>@cluster0.njdyx1x.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

'''

client = pymongo.MongoClient("mongodb+srv://LNarayan:Ganga123@cluster0.njdyx1x.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"D:\DATA_ANALYST\8th_Sem_Project_ML\Project-DataScience_FY\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
