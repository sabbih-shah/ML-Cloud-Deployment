from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.webservice import Webservice
from azureml.core.image import ContainerImage
from azureml.core.webservice import AciWebservice


workspace = Workspace.from_config("../../.azureml/config.json")

model = Model.register(model_path="../../models/XGBRegressor_model.pkl",
                       model_name="XGBRegressor_model",
                       tags={"key": "1"},
                       description="predict Predictive score",
                       workspace=workspace)

aciconfig = AciWebservice.deploy_configuration(cpu_cores=1,
                                               memory_gb=1,
                                               tags={"data": "Salary", "method": "LightGBM"},
                                               description='Predict Predictive score')

image_config = ContainerImage.image_configuration(execution_script="score.py",
                                                  runtime="python",
                                                  conda_file="../../conda_env.yml")

service = Webservice.deploy_from_model(workspace=workspace,
                                       name='predictive-model-svc',
                                       deployment_config=aciconfig,
                                       models=[model],
                                       image_config=image_config)

service.wait_for_deployment(show_output=True)

print(service.scoring_uri)
