from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
import json
# no keys required for crypto data
client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD", "ETH/USD"],
                        timeframe=TimeFrame.Day,
                        start=datetime(2022, 7, 1),
                        end=datetime(2022, 9, 1)
                 )

bars = client.get_crypto_bars(request_params)

# convert to dataframe
bars.df

# access bars as list - important to note that you must access by symbol key
# even for a single symbol request - models are agnostic to number of symbols
bars["BTC/USD"]

# Convert the dict to a JSON string
barset_json = json.dumps(bars["BTC/USD"], indent=4, default=str)  # default=str to handle datetime serialization

# Write the JSON string to a file
with open('crypto_price_data.json', 'w') as f:
    f.write(barset_json)