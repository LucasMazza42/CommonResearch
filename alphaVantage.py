import requests

def get_daily_time_series(stock_symbol, api_key):
    # Base URL for Alpha Vantage API
    base_url = "https://www.alphavantage.co/query"
    
    # Parameters for the API call
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": api_key,
        "outputsize": "full"  # Use "compact" for the last 100 data points, or "full" for the full-length time series
    }
    
    # Make the GET request
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()
        
        # You can then process this data as needed
        return data
    else:
        # Handle errors (e.g., invalid API key, wrong stock symbol)
        return None

# Example usage:
API_key = "6EVG2MQLPARM4YKW"

