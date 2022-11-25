
import pandas as pd
import numpy as np

class fill_nan:
    
        def __init__(self, df, cols):
            self.df = df
            self.cols = cols
            self.fill_nan_mean(self.cols)
        
        def fill_nan_mean(self, cols):
            
            '''
            Fill NaN with the mean value of the column in the given columns.
            
            Parameters: 
                df (dataframe): dataframe to fill NaNs for
                cols (list): target columns to fill NaNs for
                
            Returns:
                df: dataframe with filled NaN in target columns
            '''
            
            self.df.loc[:,cols].fillna(self.df.mean().iloc[0],inplace=True)

