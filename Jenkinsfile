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
                sh 'ln -s Boxer-Generator/docker-compose.yaml build'
            }
        }
    }
}4