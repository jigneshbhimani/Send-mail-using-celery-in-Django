**1)For Ubuntu:**

-> Run the server (In Terminal-1) 
python3 manage.py runserver

-> Run the celery (In Terminal-2)
celery -A project_name.celery worker -l info

Note: Everytime If you will change tasks.py file then you need to run again celery everytime.

**2)For Windows:**

-> Run the server (In cmd-1)
python manage.py runserver

-> Run the celery (In cmd-2)
pip install eventlet
celery -A project_name worker -l info -P eventlet
