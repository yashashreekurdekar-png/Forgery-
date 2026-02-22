# Data Preprocessing Utilities

import pandas as pd


def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)


def clean_data(data):
    """Clean the data by dropping missing values and duplicates."""
    data = data.dropna()
    data = data.drop_duplicates()
    return data


def feature_engineering(data):
    """Add custom features to the dataset."""
    # Example feature: you can add your logic here
    data['new_feature'] = data['existing_feature'] * 2  # Placeholder logic
    return data
