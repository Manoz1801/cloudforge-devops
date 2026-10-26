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

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloudforge:ci-${BUILD_NUMBER} .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker image inspect cloudforge:ci-${BUILD_NUMBER}'
                echo 'CloudForge Docker image built successfully!'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        set +x
                        echo "$DOCKERHUB_TOKEN" | docker login \
                            --username "$DOCKERHUB_USER" \
                            --password-stdin

                        docker tag cloudforge:ci-${BUILD_NUMBER} \
                            "$DOCKERHUB_USER/cloudforge:ci-${BUILD_NUMBER}"

                        docker push "$DOCKERHUB_USER/cloudforge:ci-${BUILD_NUMBER}"

                        docker logout
                    '''
                }
            }
        }
    }
}
