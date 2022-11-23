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


#Part D
# #%%

# from sklearn.datasets import load_iris
# import pandas as pd

# data = load_iris()
# df = pd.DataFrame(data=data.data, columns=data.feature_names)
# df.head()
# #%%
# obj=StandardScaler()
# df[['sepal length (cm)','petal width (cm)']].apply(lambda x:pd.DataFrame(obj.fit_transform(x).reshape(-1,1)))



#%%
from abc import ABC, abstractmethod
import numpy
from sklearn.preprocessing import StandardScaler 
class feature_transform(ABC):

    def __init__(self,df,cols:list) -> None:
         self.df=df
         self.cols=cols
    
    @abstractmethod
    def apply_transform(self):
        pass

class log_transform(feature_transform):

    def apply_transform(self):
        self.df[cols]=self.df[cols].apply(lambda x: np.log(x))
    
class reverse_log(feature_transform):
    def apply_transform(self):
        obj=StandardScaler()
        self.df[cols]=self.df[cols].apply(lambda x: np.exp(x))



        


#%%
#Part E
import sklearn
from sklearn.ensemble import RandomForestClassifier

# Instantiate rf
rf = RandomForestClassifier(max_depth=9, random_state=0)
             
# Fit rf to the training set    
# rf.fit(X_train, y_train) 
 
# Predict test set labels
# y_pred = rf.predict(X_test)
# modelselected=''
class model:

    def __init__(self,df,modelsel,x_cols,target,param_grid) -> None:
        self._x_cols=x_cols
        self._target=target
        self._param_grid=param_grid
        self.model=modelsel
        self.train(df)

    def train(self,df):
        X_train=df[self._x_cols]
        y_train=df[self._target]
        self.model.fit(X_train, y_train) 
        return None 

    def predict(self,x_test):
        return self.model.predict_proba(x_test[self._x_cols])


