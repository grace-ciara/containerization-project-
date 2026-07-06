## Crypto ETL Pipeline

An automated ETL pipeline built using Python, Pandas, Docker, and Aiven PostgreSQL that extracts live cryptocurrency market data from the CoinPaprika API.

### Transformations Performed
1. **Filtering**: Selected 5 target coins (`BTC`, `ETH`, `SOL`, `DOGE`, `USDT`) from the global API dataset.
2. **Extracting Prices**: Unpacked the hidden data fields inside the JSON `quotes` column to capture USD market rates.
3. **Column Renaming**: Renames columns (e.g. renaming `id` to `coin_id`) for a clean database layout.
4. **Adds a Time Tag**: Appended a modern, precise `extracted_at` UTC timestamp tracking exactly when the API snapshot occurred.
5. **Derived Columns**: Created a calculated `vol_to_market_cap_ratio` custom column to evaluate how heavily a coin is being traded.

### How to Run It

1. Configure your private database credentials inside a `.env` file in the root directory.
2. Open Docker Desktop.
3. Launch the containerized application using Git Bash:
   ```bash
   docker-compose up --build
   ```
