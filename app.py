from flask import Flask, jsonify, request
import joblib
import preprocessing


app = Flask(__name__)

@app.route("/predict", methods=['POST'])


def predict():
    req = request.get_json()
    input_data = req['data']
    input_data_df = preprocessing.preprocess(input_data)
    
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
    return "Welcome to Loan Approval App!"   

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '3000')

