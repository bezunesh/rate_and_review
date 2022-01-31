# gunicorn conf for staging/productin
command = '/home/ubuntu/project/rate_and_review/.venv/bin/gunicorn'
pythonpath = '/home/ubuntu/project/rate_and_review'
bind = '0:8080'
workers = 3