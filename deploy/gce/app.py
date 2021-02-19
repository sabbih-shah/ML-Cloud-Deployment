from flask import Flask, jsonify, request
from joblib import load
import pandas as pd
import json

app = Flask("Predict_Score_App")
model = load("../../models/XGBRegressor_model.pkl")


@app.route("/predict", methods=["POST"])
def predict():

    # workaround for the input json being an array
    dump = json.dumps(request.json)
    input_json = json.loads(dump)

    predictions = model.predict(pd.json_normalize(input_json, 'data'))

    return json.dumps({"predictions": predictions.tolist()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
