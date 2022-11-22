# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:47:43 2022

@author: herre
"""


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
        
        self.X = self.df.drop("diabetes_mellitus", axis=1)
        self.y = self.df["diabetes_mellitus"]
    
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = 0.3, random_state = 2, stratify = self.y)

# Part B

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
            
# Part C

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
            
            self.df[cols] = self.df[cols].fillna(self.df.mean().iloc[0])
            