# Carpooling Management System

This is a Web-Application built using Django framework and MySQL Database with HTML/CSS + Bootstrap front end for the CS254 DataBase Systems Lab Course (Mini-Project).

## Team members:
1. Swapnil Guduru
2. Mudit Singhal 
3. Ashutosh Anand


## Steps to host :
Make a New Folder named `Sharify`
Then run the following commands to your terminal
```
git clone https://github.com/swapnil2911/Sharify.git
cd Sharify
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
This will set up your intial project folder. 
Then in your MySQL shell, Create a database name as `cabify` and then grant all the permission to username `dbadmin` having password `123`.
( If you want a different username\password for your program, do make changes in  `DATABASES` section of `Carpooling\Carpooling\settings.py` )

Now make migrations and start the server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
``` 
This will start a local-server at 127.0.0.1:8000 hosting the project.
