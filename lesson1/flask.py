# coding: utf-8
"""
"""
import os
from flask import Flask

app = Flask('lesson1', instance_relative_config=True)
app.config.from_object('lesson1.config.common')

if 'LESSON1_CONFIG' in os.environ:
    # Load the file specified by the environment variable
    # Variables defined here will override those in the default configuration
    app.config.from_envvar('LESSON1_CONFIG')

try:
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')
except FileNotFoundError:
    pass
