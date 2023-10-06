from flask import Flask, jsonify, request
import joblib
import preprocessing
import logging

logging.basicConfig(filename='logging.log', level=logging.INFO)

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict(): 
    output = []

    try:
        req = request.get_json()
        input_data = req['data']
        logging.info("Data is received.")
    except Exception as e:
        logging.error(f"Request receiving error: {str(e)}")
        return jsonify({"error": str(e)})

    input_data_df = preprocessing.preprocess(input_data)
    logging.info("Preprocessing is done.")

    model = joblib.load('model_generation/models/decision_tree.pkl')

    try:
        predictions = model.predict(input_data_df)
        logging.info("Prediction is done.")
    except:
        logging.error("Prediction error!")
    
    
    for data, prediction in zip(input_data, predictions):
        output.append({
            "loan_id": data["loan_id"],
            "loan_status": "Approved" if prediction else "Rejected"
        })
    logging.info(f"Prediction: {output}")
    return jsonify({'output': output})

    
@app.route('/')
def home():
    return "Welcome to Loan Prediction App!"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '5000', debug=True)