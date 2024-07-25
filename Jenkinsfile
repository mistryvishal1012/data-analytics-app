pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Ensure Python and pip are installed
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Ensure pytest is installed
                    sh 'pytest'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    // Ensure Docker is running and the Dockerfile is in the right place
                    docker.build('my-python-app:latest')
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Ensure kubectl is configured to use Minikube
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
    post {
        always {
            // Clean up actions or notifications can be added here
            echo 'Pipeline completed.'
        }
    }
}
