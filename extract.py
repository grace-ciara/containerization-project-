import requests


def extract_crypto_data():
    url = "https://api.coinpaprika.com/v1/tickers?quotes=USD"

    response = requests.get(url)

    print(response.text)

    response.json()

    crypto_data = response.json()

    return crypto_data   