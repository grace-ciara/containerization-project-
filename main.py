from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_crypto_data


def main():
        crypto_data = extract_crypto_data()
        crypto_df = transform_crypto_data(crypto_data)
        load_crypto_data(crypto_df)
        print("ETL process completed successfully.")

if __name__ == "__main__":
    main()  