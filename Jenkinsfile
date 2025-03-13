
pipeline {
    agent any
    
    environment {
        AWS_REGION = 'ap-south-1'     // Change to your AWS region
        LAMBDA_FUNCTION_NAME = 'MyLambdaFunction' // Name of your Lambda function
        AWS_ACCESS_KEY_ID = credentials('aws-access-key') // AWS credentials stored in Jenkins
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'UA-1234', url: 'https://github.com/SefaliSabnam/Aws-lambda-cicd-resume.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install --target ./package boto3'
            }
        }
        
        stage('Package Lambda') {
            steps {
                sh """
                mkdir -p package
                cp lambda_function.py package/
                cd package
                zip -r ../lambda.zip .
                """
            }
        }
        
        stage('Deploy Lambda') {
            steps {
                sh """
                aws lambda update-function-code \
                    --function-name $LAMBDA_FUNCTION_NAME \
                    --zip-file fileb://lambda.zip \
                    --region $AWS_REGION
                """
            }
        }
    }

    post {
        success {
            echo ' Lambda deployed successfully!'
        }
        failure {
            echo ' Lambda deployment failed!'
        }
    }
}

