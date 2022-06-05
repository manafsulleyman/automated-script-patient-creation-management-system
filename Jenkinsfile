pipeline {
    agent any
    
    stages {
        stage{
             steps {
                 sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python tests.py'
     }
        }
        stage('test') {
            steps {
                sh 'pip install selenium && pip install selenium && pip install webdriver-manager && pip install xlrd && pip install behave'
            }
        }
    }
}


easy_install python-jenkins
