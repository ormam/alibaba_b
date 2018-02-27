pipeline {
    agent any
    environment {
        App_Name    = 'alibaba-nodejs4'
    }

    stages {
        stage('Get Dockerfile') {
            steps {
                echo 'Getting docker file'
		sh 'wget http://s3.amazonaws.com/alibabadocker/Dockerfile'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
		sh " /usr/bin/docker build -t ormaman/${App_Name}:${BUILD_NUMBER} ."
            }
        }
        stage('Push to registry') {
            steps {
                echo 'Pushing to registry..'
		sh " /usr/bin/docker login -u ormaman -p Aa123456"
		sh " /usr/bin/docker push ormaman/${App_Name}:${BUILD_NUMBER}"
            }
        }
        stage('Deploy') {
            steps {
	     	sh "  docker run -d -p 80${BUILD_NUMBER}:8080  ormaman/${App_Name}:${BUILD_NUMBER}"
	    } 
	}
	
	    stage('Test') {
            steps {
		sh "sleep 2"    
	     	sh "curl 127.0.0.1:80${BUILD_NUMBER}"
	    }
	}
	    
		    
    }
}
