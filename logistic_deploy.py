#Let's start with importing necessary libraries
import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template

class predObj:

    def predict_log(self, dict_pred):
        with open("Final_standardScalar_Logistic_Prediction.sav", 'rb') as f:
            #print('Inside Scalar')
            scalar = pickle.load(f)

        with open("modelForPrediction.sav", 'rb') as f:
            #print('INside Model')
            model = pickle.load(f)
        data_df = pd.DataFrame(dict_pred,index=[1,])
        #print(data_df)
        scaled_data = scalar.transform(data_df)
        predict = model.predict(scaled_data)
        #print(predict)
        if predict[0] ==1 :
            result = 'Diabetic'
            #print(result)
        else:
            result ='Non-Diabetic'
            #print(result)
        return result



