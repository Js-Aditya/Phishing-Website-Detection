from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('dt1.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    link= request.form.get('link')

    #prediction
    result=model.predict(np.array([link]))

    if result[0]=="good":
        result="S"
    else:
        result="P"
    return render_template('index.html',result=result)


if __name__=='__main__':
    app.run(debug=True)





