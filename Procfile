web: gunicorn errors_db.wsgi:application
worker: python manage.py rqworker default short
scheduler: python manage.py rqscheduler default short
worker_default: python manage.py rqworker default
worker_short: python manage.py rqworker short
dev_worker: honcho start -f Procfile_dev_worker
release: python manage.py migrate --noinput
