import pandas as pd
import numpy as np

def drop_nan(df: pd.DataFrame, cols: list):
    '''
    Remove those rows that contain NaN values in the given columns.
    
    Parameters: 
        df (dataframe): dataframe to remove rows for
        cols (list): target columns to remove rows for
        
    Returns:
         cleaned_df: dataframe with removed rows in target columns
    '''
    cleaned_df = df.dropna(axis=0, subset=cols, how='any')
    return cleaned_df

def fill_nan(df: pd.DataFrame, cols: list):
    '''
    Fill NaN with the mean value of the column in the given columns.
    
    Parameters: 
        df (dataframe): dataframe to fill NaNs for
        cols (list): target columns to fill NaNs for
        
    Returns:
        df: dataframe with filled NaN in target columns
    '''
    df[cols] = df[cols].fillna(df.mean().iloc[0])
    return df 
    