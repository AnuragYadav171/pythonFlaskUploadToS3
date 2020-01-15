pipeline {
   agent { dockerfile true } 
   stages {
      stage('Build') {
         steps {
            docker ps
            docker build -t anuragyadav171/devops_app:v1.0.0 .
            docker login --username='anuragyadav171' --password='Garuna@1995'
            docker push anuragyadav171/devops_app:v1.0.0
         }
      }
   }
}


