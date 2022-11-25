
from abc import ABC, abstractmethod
import numpy as np
testdata=[]
# from sklearn.preprocessing import StandardScaler 
class feature_transform(ABC):

        def __init__(self,df,cols:list) -> None:
            self.df=df
            self.cols=cols

        @abstractmethod
        def apply_transform(self):
            return NotImplementedError

class log_transform(feature_transform):

        def apply_transform(self):
            self.df.loc[:,self.cols]=self.df.loc[:,self.cols].apply(lambda x: np.log(x))
    
class reverse_log(feature_transform):

        def apply_transform(self):
            self.df.loc[:,self.cols]=self.df.loc[:,self.cols].apply(lambda x: np.exp(x))

