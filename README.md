# ML-Cloud-Deployment

This project contains implementation for performing grid search and saving the trained model for udemy scrapped dataset.
The trained model can then be deployed on both Azure machine learning and Google compute engine.

The project is structured as follows:

**1.** The model.py reads the input dataframe and selects the column according to pre-computed feature importance. It then splits the dataframe into training and test set. Finally, it performs a grid search to find the best parameters for the XGBRegressor and save it.

**2.** The deploy folder contains two sub folders for azure and gce deployment whcich is explained in the relevant section.

**Model Training:**

We use the popular XGBoost library and train a XGBRegressor to predict the predictive_score column. A grid search is performed over number of estimators, max depth and the learning rate with 5-fold cross validation. The trained model is saved in the models directory. Following are the test metrics:

R2_score:  0.97124, mean absolute error:  0.069653, explained variance:  0.971242

**Deployment:**

The model can be deployed on both Azure and google cloud.

*Azure Deplyment:*

To deploy on azure change to execute deploy.py in the deploy/azure directory. The user needs to provide a valid config file in .azureml directory and also make sure that a pretrined model is in the relevant directory. It also contains the score.py script which is usd to compute and return the predictions. An environment.yml file is also provided to create an appropriate conda environment.

*Google Compute Engine Deployment:*

The model can also be deployed on GCE. First create a project on google cloud and add a vm in the google compute engine. Then configure ssh access and deop to a terminal. Then copy and execute the deploy_gce.sh bash scrript. This clones the repositry, configure the environment and starts a Gunicorn server binfing the flask app to return the predictions from the gce vm endpoint.

**Testing:**

Two files are provided for teting the deployed model. The azure testing file contains a live endpoint for testing and the gce testing file require the user to enter the encpoint address after deployment.

