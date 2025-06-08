from alpaca.data.live import StockDataStream
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Access environment variables
ALPACA_API_KEY_ID = os.getenv('ALPACA_API_KEY_ID')
ALPACA_API_SECRET_KEY = os.getenv('ALPACA_API_SECRET_KEY')

wss_client = StockDataStream('api-key', 'secret-key')

# async handler
async def quote_data_handler(data):
    # quote data will arrive here
    print(data)

wss_client.subscribe_quotes(quote_data_handler, "SPY")

wss_client.run()