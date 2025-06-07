from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import json

# no keys required for crypto data
client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD", "ETH/USD"],
                        timeframe=TimeFrame.Day,
                        start="2025-06-05"
                 )

bars = client.get_crypto_bars(request_params)

# Convert the dict to a JSON string
barset_json = json.dumps(bars.data, indent=4, default=str)  # default=str to handle datetime serialization

# Write the JSON string to a file
with open('crypto_price_data.json', 'w') as f:
    f.write(barset_json)