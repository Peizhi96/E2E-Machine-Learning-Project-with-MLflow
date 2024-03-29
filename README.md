# E2E-Machine-Learning-Project-with-MLflow


## Workflows
1. Update config.ymal
2. Update schema.ymal
3. Update params.ymal
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

### Dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Peizhi96/E2E-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=Peizhi96 \
MLFLOW_TRACKING_PASSWORD=44dcab6c340f4887f432dc5dd04e6fcf68b9b076 \
python script.py

```
export MLFLOW_TRACKING_URI=https://dagshub.com/Peizhi96/E2E-Machine-Learning-Project-with-MLflow.mlflow 
export MLFLOW_TRACKING_USERNAME=Peizhi96
export MLFLOW_TRACKING_PASSWORD=44dcab6c340f4887f432dc5dd04e6fcf68b9b076 
```
AWS-CICD-Deployment-With-Github-Actions
## 1. Login to AWS console

## 2. Create IAM user for deploymet
    1. EC2 access: It is virtual machine
    2. ECR: Elastic container registery to save your docker image in AWS

## 3. Create ECR repo to store/save docker image
    - Save the URI: 287109008310.dkr.ecr.us-east-1.amazonaws.com/ml_project

## 4. Create EC2 machine(Ubuntu)

## 5. Open EC2 and Install docker in EC2 machine:
    #optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

## 6.Configure EC2 as self-hosted runner
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

## 7. Setup github secrets:
    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 287109008310.dkr.ecr.us-east-1.amazonaws.com

    ECR_REPOSITORY_NAME = ml_project
