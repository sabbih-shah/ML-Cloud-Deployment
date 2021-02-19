from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.webservice import Webservice
from azureml.core.image import ContainerImage
from azureml.core.webservice import AciWebservice


# create workspace fro config file (user needs to add relevant info in config file)
workspace = Workspace.from_config("../../.azureml/config.json")

# register model by name and assign tag
model = Model.register(model_path="../../models/XGBRegressor_model.pkl",
                       model_name="XGBRegressor_model",
                       tags={"key": "1"},
                       description="predict Predictive score",
                       workspace=workspace)

# configure compute resources
aciconfig = AciWebservice.deploy_configuration(cpu_cores=1,
                                               memory_gb=1,
                                               tags={"data": "Salary", "method": "LightGBM"},
                                               description='Predict Predictive score')

# configure docker image
image_config = ContainerImage.image_configuration(execution_script="score.py",
                                                  runtime="python",
                                                  conda_file="../../conda_env.yml")

# configure endpoint parameters
service = Webservice.deploy_from_model(workspace=workspace,
                                       name='predictive-model-svc',
                                       deployment_config=aciconfig,
                                       models=[model],
                                       image_config=image_config)

# wait for deployment
service.wait_for_deployment(show_output=True)

print(service.scoring_uri)
