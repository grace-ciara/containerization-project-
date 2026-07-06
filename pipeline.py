import requests
import pandas as pd
import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def extract_crypto_data():
    url = "https://api.coinpaprika.com/v1/tickers?quotes=USD"

    response = requests.get(url)

    print(response.text)

    response.json()

    crypto_data = response.json()

    return crypto_data    


def transform_crypto_data(crypto_data):
    crypto_df = pd.DataFrame(crypto_data)

    crypto_df.head()

    my_coins = ['btc-bitcoin', 'eth-ethereum', 'sol-solana', 'doge-dogecoin', 'usdt-tether']

    coins_df = crypto_df[crypto_df['id'].isin(my_coins)].copy()

    coins_df

    coins_df['price'] = [row['USD']['price'] for row in coins_df['quotes']]

    coins_df['volume'] = [row['USD']['volume_24h'] for row in coins_df['quotes']]

    coins_df['market_cap'] = [row['USD']['market_cap'] for row in coins_df['quotes']]

    coins_df[['id', 'name', 'price', 'volume', 'market_cap']]


    useful_columns = ['id', 'name', 'symbol', 'rank', 'price', 'volume', 'market_cap']

    crypto_df = coins_df[useful_columns].copy()

    crypto_df = crypto_df.rename(columns={'id': 'coin_id'})

    crypto_df

    crypto_df['extracted_at'] = pd.Timestamp.now('UTC')

    crypto_df['vol_to_market_cap_ratio'] = crypto_df['volume'] / crypto_df['market_cap']

    return crypto_df


def load_crypto_data(crypto_df):
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    crypto_df.to_sql('cryptodata_pipeline', con=engine, if_exists='replace', index=False)


def main():
    crypto_data = extract_crypto_data()
    crypto_df = transform_crypto_data(crypto_data)
    load_crypto_data(crypto_df)
    print("ETL process completed successfully.")

if __name__ == "__main__":
    main()    
