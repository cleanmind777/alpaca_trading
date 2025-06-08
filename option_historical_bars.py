from alpaca.data.historical.option import OptionHistoricalDataClient
from alpaca.data.requests import OptionBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Access environment variables
APCA_API_KEY_ID = os.getenv('APCA_API_KEY_ID')
APCA_API_SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')

# setup option clients for historical data
option_historical_data_client = OptionHistoricalDataClient(APCA_API_KEY_ID,  APCA_API_SECRET_KEY)

# currently time
now = datetime.now(tz = ZoneInfo("America/New_York"))

# symbol
option_symbol = "SPY250610C00599000"
request_params = OptionBarsRequest(
    symbol_or_symbols=[option_symbol],
    timeframe = TimeFrame(amount = 2, unit = TimeFrameUnit.Hour),
    start = now - timedelta(days = 5),
    # end = datetime.now(),
    limit= 5
)

# Fetch the option bars data
bars = option_historical_data_client.get_option_bars(request_params)

# The returned data can be accessed as a DataFrame
bars_df = bars.df

print(bars_df)

# Convert the dict to a JSON string
barset_json = json.dumps(bars[option_symbol], indent=4, default=str)  # default=str to handle datetime serialization

# Write the JSON string to a file
with open('option_price_data.json', 'w') as f:
    f.write(barset_json)