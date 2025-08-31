pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nirajneeru2009/SwagLabsUI_Automation.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                // Linux/macOS
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'

                // Windows (replace above with bat commands)
                // bat 'python -m venv venv'
                // bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/ --junitxml=reports/results.xml'
            }
        }
    }
    post {
        always {
            // Publish test results in Jenkins UI
            junit 'reports/*.xml'

            // Archive reports and screenshots
            archiveArtifacts artifacts: 'reports/**, screenshots/**', allowEmptyArchive: true
        }
    }
}
