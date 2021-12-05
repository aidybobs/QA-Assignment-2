pipeline {
    agent any


    options {
        timestamps()
    }


    environment {
        DOCKER_USERNAME = credentials('username')
        DOCKER_PASSWORD = credentials('password')
        secretkey = credentials('secretkey')

    }

    stages {
        stage('Build') {
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }

        stage('Test') {
            steps{
                sh "bash tests.sh"
            }
        }

       stage('Deploy') {
            steps {
                sh "scp -o StrictHostKeyChecking=no docker-compose.yaml dockermanager:/home/jenkins/docker-compose.yaml"
                sh "scp -o StrictHostKeyChecking=no nginx.conf dockermanager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
                cleanWs notFailBuild: true, patterns: [[pattern: 'node_modules', type: 'EXCLUDE']]
            }
       }
    }
}