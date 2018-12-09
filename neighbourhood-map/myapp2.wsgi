#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/neighbourhood-map')

from src import app as application
application.secret_key = '_5#y2Ldsfsdf'
