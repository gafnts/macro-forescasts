import os
from fredapi import Fred
from dotenv import load_dotenv


def create_fred_client() -> Fred:
    load_dotenv()
    FRED_API_KEY = os.getenv("FRED_API_KEY")
    fred = Fred(api_key=FRED_API_KEY)
    return fred
