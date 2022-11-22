import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

import warnings
warnings.filterwarnings('ignore')

def train_model(df: pd.DataFrame, feature_cols: list, target_cols: list):
    '''
    Split, fit, and train model using RandomForestClassifier.
    
    Parameters: 
        df (dataframe): dataframe to the train model for
        feature_cols (list): list of columns as features
        target_cols (list): list of columns as target
        
    Returns:
        y_train (dataframe): train dataframe from train_test_split
        y_test (dataframe): test dataframe from train_test_split
        y_train_pred_proba (array): 1d array of predicted probability for train set
        y_test_pred_proba (array): 1d array of predicted probability for test set
        
    '''
    X = df[feature_cols]
    y = df[target_cols]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2, stratify=y)
    rf_clf = RandomForestClassifier(n_estimators=500, random_state=10)
    rf_clf.fit(X_train, y_train)
    
    y_train_predicted = rf_clf.predict(X_train)
    y_train_pred_proba = np.max(rf_clf.predict_proba(X_train), axis=1)
    X_train['train_pred'] = y_train_predicted
    
    y_test_predicted = rf_clf.predict(X_test)
    y_test_pred_proba = np.max(rf_clf.predict_proba(X_test), axis=1)
    X_test['test_pred'] = y_test_predicted
    
    return(y_train, y_test, y_train_pred_proba, y_test_pred_proba)

def get_roc_auc_score(trained: tuple):
    '''
    Obtains the roc_auc metric for train and test sets.
    
    Parameters: 
        trained (tuple): arrays consisting the train model's y_train, y_test, y_train_pred_proba, y_test_pred_proba
        
    Returns:
        train_auc (float): decimal float of train auc_score
        test_auc (float): decimal float of test auc_score
        
    '''
    y_train, y_test, y_train_pred_proba, y_test_pred_proba = trained
    
    # obtain scores
    train_auc = roc_auc_score(y_train, y_train_pred_proba)
    test_auc = roc_auc_score(y_test, y_test_pred_proba)
    
    return train_auc, test_auc    
    