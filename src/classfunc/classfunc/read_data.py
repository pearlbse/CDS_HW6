# Part A

import pandas as pd
from sklearn.model_selection import train_test_split

class load_and_split:
    
    def __init__(self, file):
        self.file = file
        self.load()
        self.split()
        
    def load(self):
        
        '''
        Read database.
        
        Parameters: 
            path: path to data
            
        Returns:
            df (dataframe): database in pandas format
        '''
        
        self.df = pd.read_csv(self.file, index_col=0)
      

    def split(self):
        
        '''
        Split data between train and test using sklearn.model_selection.train_test_split.
        
        Parameters: 
            df (dataframe): dataframe to split data for
            
        Returns:
            X_train (dataframe): split X train dataframe from train_test_split
            X_test (dataframe): split X test dataframe from train_test_split
            y_train (dataframe): split y train dataframe from train_test_split
            y_test (dataframe): split y test dataframe from train_test_split
            
        '''
        
    
        self.Train,self.Test = train_test_split(self.df, test_size = 0.3, random_state = 2)
        return self.Train, self.Test

