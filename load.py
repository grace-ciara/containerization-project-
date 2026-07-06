import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()


def load_crypto_data(crypto_df):
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    crypto_df.to_sql('cryptodata_main', con=engine, if_exists='replace', index=False)