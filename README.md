# ML-Cloud-Deployment

This project contains implementation for performing grid search and saving the trained model for udemy scrapped dataset.
The trained model can then be deployed on both Azure machine learning and Google compute engine.

The project is structured as follows:

1. The model.py reads the input dataframe and selects the column according to pre-computed feature importance. It then splits the dataframe into training and test set. Finally it performs a grid search to find the best parameters for the XGBRegressor and sva it.
2. The deploy folder contains two sub folders. 

