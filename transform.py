import pandas as pd

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