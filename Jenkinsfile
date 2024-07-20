node {
    stage('Build') {
        docker.image('python:2-alpine').inside {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }

    stage('Test') {
        docker.image('qnib/pytest').inside {
            sh 'py.test sources/test_calc.py'
        }
    }

    stage('Deliver') {
        docker.image('python:3.9-slim').inside('-u root') {
            sh 'apt-get update && apt-get install -y \
                binutils \
                && apt-get clean \
                && rm -rf /var/lib/apt/lists/*'
            sh 'pip install pyinstaller'
            sh 'pyinstaller --onefile sources/add2vals.py'
        }
        archiveArtifacts 'dist/add2vals'
    }

    stage('ManualApproval') {
        input message: 'Lanjutkan ke tahap Deploy?'
    }

    stage('Deploy') {
        // sh './scripts/deploy.sh'
        docker.image('python:3.9-slim').inside('-p 3000:3000') {
            sh 'ls dist'
        }
    }
}