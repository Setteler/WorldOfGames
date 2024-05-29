pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('world-of-games')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image('world-of-games').run('-p 8777:8777 -v $WORKSPACE/Scores.txt:/Scores.txt --name world-of-games')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python e2e.py', returnStatus: true)
                    if (result != 0) {
                        error('Tests failed')
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop world-of-games'
                    sh 'docker rm world-of-games'
                    docker.image('world-of-games').push('your-dockerhub-username/world-of-games:latest')
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
