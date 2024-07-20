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
        docker.image('cdrx/pyinstaller-linux:python2').inside {
            sh 'pyinstaller --onefile sources/add2vals.py'
        }
    }

    stage('ManualApproval') {
        input message: 'Lanjutkan ke tahap Deploy? (Klik "Proceed" untuk mengakhiri)'
    }

    // stage('Deploy') {

    // }
}