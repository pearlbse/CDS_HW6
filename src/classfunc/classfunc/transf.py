
from abc import ABC, abstractmethod
import numpy as np
testdata=[]
# from sklearn.preprocessing import StandardScaler 
class feature_transform(ABC):
    
        @abstractmethod
        def apply_transform(self):
            return NotImplementedError

class log_transform(feature_transform):

        def __init__(self,df,cols:list) -> None:
            self.df=df
            self.cols=cols

        def apply_transform(self):
            self.df.loc[:,self.cols]=self.df.loc[:,self.cols].apply(lambda x: np.log(x))
    
class reverse_log(feature_transform):

        def __init__(self,df,cols:list) -> None:
            self.df=df
            self.cols=cols
            
        def apply_transform(self):
            # obj=StandardScaler()
            self.df.loc[:,self.cols]=self.df.loc[:,self.cols].apply(lambda x: np.exp(x))

