kill -9 $(lsof -i:8080 |awk '{print $2}' | tail -n 2)

cd /home/ec2-user/webservice/

sudo rm -rf ./app

sudo systemctl stop amazon-cloudwatch-agent.service

sudo rm ./cloudwatch-config.json