pipeline {
    agent any
    stages{
        stage('version'){
            steps{
                bat 'python3 --version'
                }
            }
        stage('clone wars'){
            steps{
                bat 'python3 clones.py'
                }
            }
        }
    }
