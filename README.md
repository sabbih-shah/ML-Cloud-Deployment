# ML-Cloud-Deployment

This project contains implementation for performing grid search and saving the trained model for udemy scrapped dataset.
The trained model can then be deployed on both Azure machine learning and Google compute engine.

The project is structured as follows:

**1.** The `model.py` reads the input dataframe and selects the column according to pre-computed feature importance. It then splits the dataframe into training and test set. Finally, it performs a grid search to find the best parameters for the XGBRegressor and save it.

**2.** The deploy folder contains two subfolders for azure and gce deployment which is explained in the relevant section.

To configure the environment locally for testing clone and then change directory to repository root and execute: 


`conda env create -f conda_env.yml`

`conda activate production_environment`


**Model Training:**

We use the popular XGBoost library and train a XGBRegressor to predict the predictive_score column. A grid search is performed over the number of estimators, max depth and the learning rate with 5-fold cross-validation. The trained model is saved in the models directory. Following are the test metrics:

`R2_score:  0.97124, mean absolute error:  0.069653, explained variance:  0.971242`

To enable training set the `TRAIN` flag to true in the `model.py` script and execute it.

**Deployment:**

The model can be deployed on both Azure and google cloud.

*Azure Deployment:*

To deploy on azure change to execute `deploy.py` in the `deploy/azure directory`. The user needs to provide a valid config file in the `.azureml` directory and also make sure that a pre-trained model is in the relevant directory. It also contains the `score.py` script which is used to compute and return the predictions. An `environment.yml` file is also provided to create an appropriate conda environment.

*Google Compute Engine Deployment:*

The model can also be deployed on GCE. First, create a project on google cloud and add a VM in the google compute engine. Then configure ssh access and drop to a terminal. Then copy and execute the `deploy_gce.sh` bash script. This clones the repository, configure the environment and starts a Gunicorn server binding the flask app to return the predictions from the gce VM endpoint.

**Testing:**

Two files are provided for testing the deployed model. The azure testing file contains a implementation for testing and the gce testing file requires the user to enter the endpoint address after deployment. To test the azure endpoint change url to live endpoint and just execute the `test_azure_endpoint.py`.

