import uwsgi
from uwsgidecorators import filemon

@filemon('run.py')
def reloaded(num):
    uwsgi.reload()
