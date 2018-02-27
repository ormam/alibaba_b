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
		sh "docker build -t ormaman/${App_Name}:${BUILD_NUMBER} ."
            }
        }
        stage('Push to registry') {
            steps {
                echo 'Pushing to registry..'
		sh "docker login -u ormaman -p Aa123456"
		sh "docker push ormaman/${App_Name}:${BUILD_NUMBER}"
            }
        }
    }
}
