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

    predictions = model.predict(input_data_df)

    output = []

    for data, prediction in zip(input_data, predictions):
        output.append({
            "loan_id": data["loan_id"],
            "loan_status": "Approved" if prediction else "Rejected"
        })

    return jsonify({'output': output})

@app.route('/')
def home():
    return "Welcome to Loan Approval App"   

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '3000')

