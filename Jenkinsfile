pipeline {
    agent any


    options {
        timestamps()
    }


    environment {
        DOCKER_USERNAME = credentials('username')
        DOCKER_PASSWORD = credentials('password')

    }

    stages {
        stage('Build') {
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }

        stage('Config/Deploy') {
            steps {
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }

    }
}