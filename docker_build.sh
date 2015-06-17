
sudo docker build -t     login/pyramid .
sudo docker run -d -t -i login/pyramid pserve production.ini

