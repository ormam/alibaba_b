pipeline {
    agent any
    environment {
        App_Name    = 'alibaba-nodejs4'
    }

    stages {
        stage('Get Dockerfile') {
            steps {
                echo 'Getting docker file'
		sh 'wget https://raw.githubusercontent.com/itamary/examples/master/Dockerfile'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
		sh "/usr/bin/sudo /usr/bin/docker build -t ormaman/${App_Name}:${BUILD_NUMBER} ."
            }
        }
        stage('Push to registry') {
            steps {
                echo 'Pushing to registry..'
		sh "/usr/bin/sudo /usr/bin/docker login -u ormaman -p Aa123456"
		sh "/usr/bin/sudo /usr/bin/docker push ormaman/${App_Name}:${BUILD_NUMBER}"
            }
        }
    }
}
