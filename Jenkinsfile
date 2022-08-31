pipeline {
    agent any
    stages{
        stage('version'){
            steps{
                sh 'python3 --version'
                }
            }
        stage('clone wars'){
            steps{
                sh 'python3 clones.py'
                }
            }
        }
    }
