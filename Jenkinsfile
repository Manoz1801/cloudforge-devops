pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate Project') {
            steps {
                sh 'test -f Dockerfile'
                sh 'test -f k8s/cloudforge.yaml'
                echo 'CloudForge project files verified!'
            }
        }
    }
}
