import pandas as pd

def gen_ohe(df: pd.DataFrame, cols: list):
    '''
    Generate dummies using one hot encoding.
    
    Parameters: 
        df (dataframe): dataframe to generate one hot encoding dummies for
        cols (list): list of columns to generate dummies
        
    Returns:
        dummies_df: dataframe with dummy column added
    '''
    dummies_df = pd.get_dummies(df, columns=cols)
    return dummies_df

def gen_binary(df: pd.DataFrame, cols: list):
    '''
    Generate binary dummies.
    
    Parameters: 
        df (dataframe): dataframe to generate binary dummies for
        cols (list): list of columns to generate dummies
        
    Returns:
        dummies_df: dataframe with dummy column added
    '''
    dummies_df = pd.get_dummies(df, columns=cols)
    return dummies_df
    