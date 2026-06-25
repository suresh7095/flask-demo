pipeline {
    agent any

    stages {

        stage('Checkout') {
    steps {
        git branch: 'main', url: 'https://github.com/suresh7095/flask-demo.git'
    }
}

        stage('Build') {
            steps {
                bat 'docker build -t flask-demo:latest .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker ps'
            }
        }
    }
}