Practical Django 2 and Channels 2, Apress PDF
1/25, Fri

pg38   

#path
cd /home/hal/Documents/softwares/pycharm/workspace/booktime; source ~/venv3.6/bin/activate

#postgresql
sudo su postgres
psql -d booktime

sudo systemctl start postgresql
docker-compose exec database psql -U postgres -h database