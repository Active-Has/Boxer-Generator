pipeline{
    agent any
    stages{
        stage('Stage1-testing') {
            steps{
                sh 'bash script/test.sh'
            }
        }
        stage('Stage2-docker') {
            steps{
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        }
        stage('Stage3-ansible') {
            stage('ansible configuration') {
            steps {
                sh "bash ansible.sh"
            }
        }
    }
}