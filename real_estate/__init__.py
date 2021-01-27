import logging
import pickle
import azure.functions
import pandas as pd
import joblib
import json
import numpy as np

def main(req: azure.functions.HttpRequest):

    # load the model
    model = joblib.load('linear_reg.pkl')

    # gather new sample
    age = float(req.params['Age'])
    dist = float(req.params['Dist'])
    num_stores = float(req.params['Num_stores'])
    lat = float(req.params['Lat'])
    long_ = float(req.params['Long'])

    X_new = [[age,dist,num_stores,lat,long_]]

    
    # score on the new sample
    pred = model.predict(X_new)

    return np.array_str(pred)


