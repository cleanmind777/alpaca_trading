from alpaca.data.live import CryptoDataStream
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Access environment variables
ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_API_SECRET_KEY = os.getenv('ALPACA_API_SECRET_KEY')

# symbol
crypto_symbol = "BTC/USD"

wss_client = CryptoDataStream(ALPACA_API_KEY, ALPACA_API_SECRET_KEY)

# async handler
async def quote_data_handler(data):
    # quote data will arrive here
    print(data)

wss_client.subscribe_quotes(quote_data_handler, "BTC/USD")

wss_client.run()