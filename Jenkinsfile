pipeline {
    agent any
     steps {
          sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python tests.py'
     }
    stages {
        stage('test') {
            steps {
                sh 'pip install selenium && pip install selenium && pip install webdriver-manager && pip install xlrd && pip install behave'
            }
        }
    }
}


