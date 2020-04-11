pwd
date
sudo su
whoami
cd /var/lib/jenkins/workspace/GitRepoProj/app/lambda
pwd
kill -9 `ps -ef | grep -v grep | grep "lambda" | awk '{print $2}'`
python uploadFileToS3.py
