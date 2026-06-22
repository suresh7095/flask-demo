pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/youruser/flask-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                wsl docker build -t flask-demo:latest .
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                wsl docker rm -f flaskapp || true
                wsl docker run -d -p 5000:5000 --name flaskapp flask-demo:latest
                '''
            }
        }

    }
}
