import pandas as pd
import numpy as np

def calculate_moving_average(data, window_size=14, method='simple'):
    """
    Calculate moving averages for stock data.

    Parameters:
    data (DataFrame): Stock data.
    window_size (int): Number of periods over which to calculate the average.
    method (str): Type of moving average ("simple" or "exponential").

    Returns:
    Series: Calculated moving average values.
    """
    if method == 'simple':
        return data['Close'].rolling(window=window_size).mean()
    elif method == 'exponential':
        return data['Close'].ewm(span=window_size, adjust=False).mean()
    else:
        raise ValueError("Unsupported method. Use 'simple' or 'exponential'.")

def calculate_rsi(data, periods=14):
    """
    Calculate the Relative Strength Index (RSI) for stock data.

    Parameters:
    data (DataFrame): Stock data.
    periods (int): Number of periods over which to calculate RSI.

    Returns:
    Series: RSI values.
    """
    close_delta = data['Close'].diff()
    gain = (close_delta.where(close_delta > 0, 0)).rolling(window=periods).mean()
    loss = (-close_delta.where(close_delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_bollinger_bands(data, window_size=20):
    """
    Calculate Bollinger Bands for stock data.

    Parameters:
    data (DataFrame): Stock data.
    window_size (int): Number of periods to use in the rolling window.

    Returns:
    tuple: A tuple containing the upper band, middle band, and lower band.
    """
    middle_band = data['Close'].rolling(window=window_size).mean()
    std_dev = data['Close'].rolling(window=window_size).std()
    upper_band = middle_band + (std_dev * 2)
    lower_band = middle_band - (std_dev * 2)
    return upper_band, middle_band, lower_band

def calculate_macd(data, slow=26, fast=12):
    """
    Calculate the Moving Average Convergence Divergence (MACD) for stock data.

    Parameters:
    data (DataFrame): Stock data.
    slow (int): Number of periods for the slow moving average.
    fast (int): Number of periods for the fast moving average.

    Returns:
    tuple: A tuple containing the MACD line and signal line.
    """
    exp1 = data['Close'].ewm(span=fast, adjust=False).mean()
    exp2 = data['Close'].ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal
