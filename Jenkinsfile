pipeline {
    agent any
    environment {
	App_Name    = 'alibaba-nodejs4'
    }
    stages {
	stage('Get Dockerfile') {
	    steps {
		echo 'Getting docker file'
		sh 'pwd' 
		sh 'ls -l' 
		sh 'wget http://s3.amazonaws.com/alibabadocker/deepinstinct/Dockerfile'
	    }
		post{
			success{
				echo 'Docker file addmited'
			}
			failure {
			    echo ' Docker file addmission failed.'
			}
		}

	}
	stage('Build') {
	    steps {
		echo 'Building..'
		sh " /usr/bin/docker build -t ormaman/${App_Name}:${BUILD_NUMBER} ."
	    }
		post {
			success{
				  echo 'Build success'
			}
			failure {
				 echo ' Build success failed.'
			}
		}
	}
	stage('Push to registry') {
	    steps {
		echo 'Pushing to registry..'
		sh " /usr/bin/docker login -u ormaman -p Aa123456"
		sh " /usr/bin/docker push ormaman/${App_Name}:${BUILD_NUMBER}"
	    }
	   post{ 
		success{
			  echo 'Push to registry done'
		}
		failure {
			 echo ' Push to registry failed.'
		}
	   }
	}

	stage('Deploy') {
		steps {
		    timeout(time:5, unit:'DAYS'){
		    input message:'Approve Dokcer PRODUCTION Deployment?'
		    }
			sh " ssh 172.31.93.0 -l ec2-user docker run -d -p 80${BUILD_NUMBER}:8080  ormaman/${App_Name}:${BUILD_NUMBER}"
			//sh " docker run -d -p 80${BUILD_NUMBER}:8080  ormaman/${App_Name}:${BUILD_NUMBER}"
		   } 

	}

	    stage('Health check') {
	    steps {
		sh "sleep 6"    
		//sh "curl 127.0.0.1:80${BUILD_NUMBER}"
		sh "curl  172.31.93.0:80${BUILD_NUMBER}"
		echo "Try to surf to 18.206.39.31:80${BUILD_NUMBER}"
	    }
		post{
			success{
				echo 'server running !!!'
			}
			failure {
			    sh " export Docker_Temp= ormaman/${App_Name}:${BUILD_NUMBER} "
			    sh " docker kill ` docker ps | grep -i \$Docker_Temp | awk '{print \$1}'` "
			    echo 'server failed..'
			}
		}
	}
    }
}

