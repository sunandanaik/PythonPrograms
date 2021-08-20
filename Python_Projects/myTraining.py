import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data,ratio):
    np.random.seed(42)
    shuffled =np.random.permutation(len(data))
    test_set_size=int(len(data)*ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]

if __name__=='__main__':
    #Read the data
    df=pd.read_csv('data.csv')
    train,test=data_split(df,0.2)
    x_train = train[['fever','bodyPain','age','runnyNose','diffBreathe']].to_numpy()
    x_test=test[['fever','bodyPain','age','runnyNose','diffBreathe']].to_numpy()
    y_train = train[['infectionProbability']].to_numpy().reshape(2,)
    y_test = train[['infectionProbability']].to_numpy().reshape(1,)
    clf=LogisticRegression()
    clf.fit(x_train,y_train)
    #Code for inference
    inputFeatures= [102,1,22,-1,1]
    infProb=clf.predict_proba([inputFeatures][0][1])