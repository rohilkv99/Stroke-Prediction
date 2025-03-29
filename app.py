from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('req_model.sav','rb'))

@app.route('/')

def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict',methods = ['POST','GET'])
def predict():
    gender = float(request.form(['gender']))
    age	= float(request.form(['age']))
    hypertension = float(request.form(['hypertension']))
    heart_disease = float(request.form(['heart_disease']))
    marital_status = float(request.form(['marital_status']))
    work_type = float(request.form(['work_type']))
    residence_type = float(request.form(['residence_type']))
    avgglucose_level = float(request.form(['avgglucose_level']))
    bmi	= float(request.form(['bmi']))
    smoking_status = float(request.form(['smoking_status']))

    result = model.predict([[gender,age,hypertension,heart_disease,marital_status,work_type,residence_type,avgglucose_level,bmi,smoking_status]])

    return render_template('index.html',**locals())


if __name__ == '__main__':
    app.run(debug =True)