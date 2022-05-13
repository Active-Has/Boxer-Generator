pipeline{
    agent any
    stages{
        stage('Stage1-testing') {
            steps{
                sh 'bash script/test.sh'
            }
        }
        stage('Stage2-docker') {
            environment{
                DOCKER_USERNAME = credentials('docker_username')
                DOCKER_PASSWORD = credentials('docker_password')
            }
            steps{
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }
        stage('Stage3-ansible') {
            steps {
                sh "bash ansible.sh"
                }
        }
        stage('Stage4-Deployment'){
            steps{
                // sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
                // sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-master:/home/jenkins/nginx.conf"
                sh "scp -i ~/ansible_ssh docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/ansible_ssh nginx.conf swarm-manager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
    }
}