Practical Django 2 and Channels 2, Apress PDF
3/09, Sat

pg39   

http://localhost:8000

#path
cd /home/hal/Documents/softwares/pycharm/workspace/booktime; source ~/venv3.6/bin/activate

#postgresql
sudo su postgres
psql -d booktime

docker-compose exec web python manage.py test
docker-compose exec database psql -U postgres -h database
docker-compose exec web python manage.py migrate
docker-compose up
docker-compose exec web python manage.py test -v 2
#logs
    docker-compose logs redis
    
    docker-compose up logs -f database
    docker-compose up logs -f web











#misc
docker build -t docker_rails .
docker-compose logs -f web
docker-compose build web //rebuilding image

docker-compose stop
docker-compose ps
docker-compose up -d database
docker-compose run --rm database psql -U postgres -h database
#logs
    docker-compose logs redis
    docker-compose up logs -f database
    docker-compose up logs -f web
#env    
mkdir -p .env/development, pg77
docker-compose run --rm web bin/rails db:create, pg78
docker-compose up -d --force-recreate web   --recreate container web
docker-compose exec web bin/rails g scaffold User first_name:string last_name:string, pg80
docker-compose exec web python manage.py migrate
docker-compose stop database
docker-compose rm -f database  - removes database from container, wipes out database and data, pg83
docker-compose up -d database
docker-compose up -d web
