import matplotlib.pyplot as plt

def plot_stock_data(data, ticker, moving_averages=None):
    """
    Plot stock data along with optional moving averages.

    Parameters:
    data (DataFrame): Stock data containing at least a 'Close' column.
    ticker (str): Stock ticker symbol for labeling the plot.
    moving_averages (list of Series, optional): List of Pandas Series representing
        different moving averages. Each series must be the same length as `data`.

    Displays:
    A matplotlib plot of the closing prices along with overlays of moving averages.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')

    if moving_averages is not None:
        for ma in moving_averages:
            plt.plot(ma, label=f'{ma.name} Moving Average')

    plt.title(f'Stock Price and Moving Averages for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()
