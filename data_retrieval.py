import yfinance as yf
from .exceptions import DataRetrievalError

def fetch_stock_data(ticker, start_date, end_date, interval='1d'):
    """
    Fetch stock data from Yahoo Finance.

    Parameters:
    ticker (str): Stock ticker symbol.
    start_date (str): Start date for data retrieval in 'YYYY-MM-DD' format.
    end_date (str): End date for data retrieval in 'YYYY-MM-DD' format.
    interval (str): Data interval (e.g., '1d' for daily data).

    Returns:
    DataFrame: Retrieved stock data.

    Raises:
    DataRetrievalError: If no data is found or an error occurs during the fetch.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
        if data.empty:
            raise DataRetrievalError(f"No data found for ticker {ticker}. Check if the ticker symbol is correct.")
        return data
    except ValueError as ve:
        raise DataRetrievalError(f"ValueError: {ve}")
    except Exception as e:
        raise DataRetrievalError(f"An error occurred while fetching data: {str(e)}")
