from flask import Flask ,jsonify,request

import config
from Project1.utils import Defaulter
import numpy as np

app = Flask(__name__)

@app.route("/")
def get_home():
    return("Namaste")

@app.route("/predict_outcome", methods = ["POST","GET"])


def get_defaulter():
    if request.method== "POST":
        data = request.form 
        Gender = data["Gender"]
        Married = data["Married"]
        Dependents = int(data["Dependents"])
        Education = data["Education"]
        Self_Employed = data["Self_Empolyed"]
        ApplicantIncome = eval(data["ApplicantIncome"])
        CoapplicantIncome = eval(data["CoapplicantIncome"])
        LoanAmount = eval(data["LoanAmount"])
        Loan_Amount_Term = eval(data["Loan_Amount_Term"])
        Credit_History = eval(data["Credit_History"])
        Propert_Area = data["Property_Area"]
        Defaulter_obj = Defaulter(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Propert_Area)  
        pred_defaulter = Defaulter_obj.get_predicted_outcome()
        return jsonify ({"Result" : f"The customer is defaulter or not {pred_defaulter}"})
    else:
        data = request.form 
        Gender = data["Gender"]
        Married = data["Married"]
        Dependents = int(data["Dependents"])
        Education = data["Education"]
        Self_Employed = data["Self_Empolyed"]
        ApplicantIncome = eval(data["ApplicantIncome"])
        CoapplicantIncome = eval(data["CoapplicantIncome"])
        LoanAmount = eval(data["LoanAmount"])
        Loan_Amount_Term = eval(data["Loan_Amount_Term"])
        Credit_History = eval(data["Credit_History"])
        Propert_Area = data["Property_Area"]
        Defaulter_obj = Defaulter(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Propert_Area)  
        pred_defaulter = Defaulter_obj.get_predicted_outcome()
        return jsonify ({"Result" : f"The customer is defaulter or not {pred_defaulter}"})



if __name__ == "__main__":
    app.run(debug=True)
