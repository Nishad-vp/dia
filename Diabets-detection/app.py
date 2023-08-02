from flask import Flask,render_template,request
import numpy as np
import pickle
from joblib import load
app=Flask(__name__)

model = pickle.load(open('Diabetes_model.pkl','rb'))
# Route

@app.route("/")
def home():
    return render_template('index.html')



@app.route("/status", methods=['POST'])
def status():
    # if request.method=="POST":
    #     sugar = int(request.form['sugar'])
    #     bp= int(request.form['bp'])
    #     insulin = int(request.form['insulin'])
    #     age = int(request.form['age'])
      

    #     # input_data = (sugar,bp,insulin,age)
    #     ## Change to numpy array
    #     input_data_array= np.array(sugar,bp,insulin,age)

    #     #Reshape
    #     # input_data_reshape = input_data_array.reshape(1,-1)
    #     prediction=model.predict(input_data_array)
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