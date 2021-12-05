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
        stage('Test') {
            steps{
                sh 'sudo apt update -y'
                sh 'sudo apt install python3 python3-pip python3-venv -y'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip3 install -r testrequirements.txt'
                sh 'python3 -m pytest archetype/tests/tests.py --cov'
                sh 'python3 -m pytest character/tests.py --cov'
                sh 'python3 -m pytest flask-app/tests/tests.py --cov'
                sh 'python3 -m pytest race/tests/tests.py --cov'
            }
        }

        stage('Build') {
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
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