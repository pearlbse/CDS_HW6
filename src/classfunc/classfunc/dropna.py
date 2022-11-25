
import pandas as pd
import numpy as np

class remove_nan:
    
        def __init__(self, df, cols):
            self.df = df
            self.cols = cols
            self.drop_nan(self.cols)
            
        def drop_nan(self, cols):
            
            '''
            Remove those rows that contain NaN values in the given columns.
            
            Parameters: 
                df (dataframe): dataframe to remove rows for
                cols (list): target columns to remove rows for
                
            Returns:
                 cleaned_df: dataframe with removed rows in target columns
            '''
            
            self.cleaned_df = self.df.dropna(axis = 0, subset = cols, how = 'any')
            