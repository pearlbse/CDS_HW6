import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import pandas as pd

# Instantiate rf
rf = RandomForestClassifier()
hyperparams = {
    'max_depth': 9,
    'n_estimators': 15,
    'min_samples_split': 3,
    'random_state': 0
}
             
class model():

    def __init__(self,Train,modelsel,x_cols,target,hyperparams = {}) -> None:
        self._x_cols=x_cols
        self._target=target
        self._hyperparams=hyperparams
        # if self._hyperparams is None:
        #     self._hyperparams = {}
        self.model=modelsel
        self.model.set_params(**self._hyperparams)
        self.train(Train)

    def train(self,Train):
        X_train=Train[self._x_cols]
        y_train=Train[self._target]
        self.model = self.model.fit(X_train, y_train) 
        return None 

    def predict(self,Test):
        self.y_test=Test[self._target]
        X_test=Test[self._x_cols]
        self.test_proba=self.model.predict_proba(X_test[self._x_cols])[:,1]
        return self.test_proba

    def get_roc_auc_score(self):
        '''
        Obtains the roc_auc metric for  test sets.
            
        '''
        # obtain scores
        test_auc = roc_auc_score(self.y_test, self.test_proba)
        
        return test_auc    

