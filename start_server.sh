export MYSQL_ROOT_PASSWORD=root
export MYSQL_DATABASE=userdb
export MYSQL_USER=root
export MYSQL_PASSWORD=qwerty@123
export MYSQL_HOST=db
source venv/bin/activate
python app/manage.py runserver
