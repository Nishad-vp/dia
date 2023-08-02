from flask import Flask,render_template,request
import numpy as np
import pickle
import pandas as pd
app=Flask(__name__)

model = pickle.load(open('Diabetes_model.pkl','rb'))

dataset = pd.read_csv('diabetes.csv')

dataset_x = dataset.iloc[:,[1, 2, 4, 7]].values

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
dataset_scaled = sc.fit_transform(dataset_x)
# Route

@app.route("/")
def home():
    return render_template('index.html')



@app.route("/status", methods=['POST'])
def status():
  
    features=[
        float(x) for x in request.form.values()
    ]
    final=[np.array(features)]
    prediction=model.predict(sc.transform(final))
    if prediction==0:
        result = "No Disease"
    else:
        result="You Have Diabetes"
    return render_template('result.html',result=result)    

    

if __name__== '__main__':
    app.run(debug=True)