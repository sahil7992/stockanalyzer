class DataRetrievalError(Exception):
    """
    Exception raised for errors that occur during data retrieval.

    Attributes:
        message (str): Explanation of the error
    """
    def __init__(self, message="Error occurred while fetching data"):
        self.message = message
        super().__init__(self.message)
