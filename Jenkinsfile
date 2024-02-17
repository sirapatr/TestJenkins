pipeline{
    agent any
    stages{
        stage("ONE"){
            agent{
                label 'vm2-tester'
            }
            steps{
                sh 'python3 -m venv myenv'
            }
        }
        stage("TWO") {
            agent {
                label 'vm2-tester'
            }
            steps {
                sh '''#!/bin/bash
                 source myenv/bin/activate && pip install -r ./requirements.txt
                
                '''
            }
        }
    }
    
}