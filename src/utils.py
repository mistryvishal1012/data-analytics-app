import pandas as pd

def load_data(filepath):
    """
    Load data from a CSV file.
    
    :param filepath: Path to the CSV file.
    :return: DataFrame containing the data.
    """
    data = pd.read_csv(filepath)
    return data

def check_for_missing_values(data):
    """
    Check for missing values in the dataset.
    
    :param data: DataFrame to check.
    :return: Series with missing value counts.
    """
    return data.isnull().sum()

def get_basic_statistics(data):
    """
    Get basic statistics for the dataset.
    
    :param data: DataFrame to analyze.
    :return: DataFrame with basic statistics.
    """
    return data.describe()
