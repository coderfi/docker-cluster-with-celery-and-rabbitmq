from __future__ import absolute_import
from celery import Celery

print "in celery.py"
app = Celery('test_celery')
app.config_from_object('celeryconfig')

