from src.logger import logging
from src.exception import user_exception
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
import sys
import os
try :
    @dataclass
    class data_ingestion :
        def initiate_data_ingestion(self) :
            directory="data_folder"
            path = os.path.join(directory)
            os.makedirs(path,exist_ok=True)



    @dataclass
    class connecting_db :
        def connection(self) :
            cloud_config={
                    'secure_connect_bundle': 'secure-connect-fraud-detection.zip'

            }
            with open("config.json") as f:
                secrets = json.load(f)
            CLIENT_ID = secrets["client_id"]
            CLIENT_SECRET = secrets["client_secret"]

            auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()

            row = session.execute("select release_version from system.local").one()
            if row :
                print(row[0])
            else :
                print("An error occured")
except :
     exception1 = user_exception()
     logging.info(exception1.show_exception())


if __name__=='__main__' :
    data_folder = data_ingestion()
    data_folder.initiate_data_ingestion()

    database = connecting_db()
    database.connection()



