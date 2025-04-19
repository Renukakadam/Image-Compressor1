pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m unittest discover -s . -p "test.py"'  // Run all tests from test.py
            }
        }

        stage('Run Script') {
            steps {
                bat 'python app\\main.py'  // Start the app if necessary
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }

        failure {
            echo 'Build failed!'
        }
    }
}

