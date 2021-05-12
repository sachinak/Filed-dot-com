# Filed-dot-com
Assignment for filed dot com

Requirements:

asgiref==3.3.4 \n
Django==3.2.2 
django-mysql==3. 11.1
djangorestframework==3.12.4
object-detection==0.1 
pytz==2021.1
sqlparse==0.4.1
typing-extensions==3.10.0.0

Commands:

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

APIs:

/api/audio/<str:type>/<int:id>
types allowed: "audiofile", "song", "podcast"


