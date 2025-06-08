from alpaca.data.historical.option import OptionHistoricalDataClient
from alpaca.data.requests import OptionBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Access environment variables
APCA_API_KEY_ID = os.getenv('APCA_API_KEY_ID')
APCA_API_SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')

option_historical_data_client = OptionHistoricalDataClient(APCA_API_KEY_ID,  APCA_API_SECRET_KEY)

# # no keys required for crypto data
# client = OptionHistoricalDataClient()

request_params = OptionBarsRequest(
    symbol_or_symbols=["SPY250606C00599000"],  # Example option contract symbol
    timeframe=TimeFrame.Hour,                 # TimeFrame can be Minute, Hour, or Day
    start=datetime(2025, 6, 1, 9, 30),          # Start datetime (e.g., June 1, 2023 9:30 AM)
    end=datetime(2025, 6, 7, 16, 0)              # End datetime (e.g., June 1, 2023 4:00 PM)
)

# Fetch the option bars data
bars = option_historical_data_client.get_option_bars(request_params)

# The returned data can be accessed as a DataFrame
bars_df = bars.df

print(bars_df)

# Convert the dict to a JSON string
barset_json = json.dumps(bars['SPY250606C00599000'], indent=4, default=str)  # default=str to handle datetime serialization

# Write the JSON string to a file
with open('option_price_data.json', 'w') as f:
    f.write(barset_json)