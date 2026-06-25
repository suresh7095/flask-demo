pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/suresh7095/flask-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-demo:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                docker stop flaskapp 2>nul
                docker rm flaskapp 2>nul

                docker run -d ^
                --name flaskapp ^
                -p 5000:5000 ^
                flask-demo:latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'docker ps'
            }
        }
    }
}