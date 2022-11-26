import sklearn
from sklearn.ensemble import RandomForestClassifier

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
        self.model.set_params(**hyperparams)
        self.train(Train)

    def train(self,Train):
        X_train=Train[self._x_cols]
        y_train=Train[self._target]
        self.model = self.model.fit(X_train, y_train) 
        return None 

    def predict(self,Test):
        X_test=Test[self._x_cols]
<<<<<<< HEAD
        return self.model.predict_proba(X_test[self._x_cols])
=======
        return self.model.predict_proba(X_test[self._x_cols])
>>>>>>> main
