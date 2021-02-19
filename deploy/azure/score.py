import pandas as pd
from joblib import load
import json
from azureml.core.model import Model


# Load the model using the saved name
def init():
    global model
    print('in init')
    model_path = Model.get_model_path('XGBRegressor_model')
    model = load(model_path)
    print('model loaded successfully')


# read json data and predict
def run(data):
    print("reading data")
    data = json.loads(data)
    data = pd.read_json(data)
    predictions = model.predict(data)
    print('predictions successful')

    # return predictions as a list
    return json.dumps({"predictions": predictions.tolist()})
