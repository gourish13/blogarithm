web: uwsgi --http-socket :$PORT --wsgi 'main:app_factory()' --die-on-term --memory-report --master --processes 2 --threads 5
