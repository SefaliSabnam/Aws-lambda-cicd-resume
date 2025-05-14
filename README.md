# AWS Lambda CI/CD - Resume

This project demonstrates a complete CI/CD pipeline for deploying an AWS Lambda function using Jenkins. The Lambda function is written in Python and is automatically deployed using the pipeline.

## Project Structure

```
Aws-lambda-cicd-resume
├── Jenkinsfile          # Jenkins pipeline configuration
├── lambda_function.py   # AWS Lambda function code
└── README.md            # Project documentation
```

## Features

* AWS Lambda function written in Python
* Jenkins for CI/CD
* Automated deployment using Jenkins pipeline

## Prerequisites

* AWS account
* Jenkins installed and configured
* IAM role with necessary permissions for Lambda

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Aws-lambda-cicd-resume
```

### 2. Configure Jenkins Pipeline

* Create a new pipeline job in Jenkins.
* Set the pipeline script path to `Jenkinsfile`.

### 3. Update AWS Credentials

* Ensure Jenkins has access to your AWS credentials.
* Configure the AWS credential ID in Jenkins.

### 4. Run the Pipeline

* Trigger the Jenkins pipeline.
* Monitor the stages (Build, Deploy).

### Lambda Function

* The Lambda function (`lambda_function.py`) is a simple Python script that can be customized.

## Usage

* Modify the `lambda_function.py` as needed.
* Use Jenkins to redeploy the Lambda function with any changes.


