from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)

@app.route("/predict", methods=['POST'])

def predict():
    req = request.get_json()
    input_data = req['data']
    input_data_df = pd.DataFrame.from_dict(input_data)
    
    input_data_df['education'] = input_data_df['education'].apply(lambda x: 1 if x == 'Graduate' else 0)
    input_data_df['self_employed'] = input_data_df['self_employed'].apply(lambda x: 1 if x == 'Yes' else 0)

    model = joblib.load('models/log_reg.pkl')

    prediction = model.predict(input_data_df)

    if prediction[0] == 1:
        loan_status = 'Approved'
    else:
        loan_status = 'Rejected'

    return jsonify({'output ':{'loan_status': loan_status}})

@app.route('/')
def home():
    return "Welcome to Loan Approval App"   

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '3000')

