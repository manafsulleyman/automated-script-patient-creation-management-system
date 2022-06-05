pipeline {
    agent {
          docker {
               image 'qnib/pytest'
          }
     }
     steps {
          sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python tests.py'
     }
    stages {
        stage('test') {
            steps {
                sh 'easy_install pip && pip install selenium && pip install selenium && pip install webdriver-manager && pip install xlrd && pip install behave'
            }
        }
    }
}


