pipeline{
    agent any
    stages('Stage1-testing') {
        steps{
            sh 'bash script/test.sh'
        }
    }
    stages('Stage2-docker') {
        environment {
            DOCKER_USERNAME = credentials('docker_username')
            DOCKER_PASSWORD = credentials('docker_password')
        }
        steps{
            sh "docker-compose build --parallel"
            sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
            sh "docker-compose push"
        }
    }
}