import os
from flask import Flask
from flask import render_template
 
app = Flask(__name__)

@app.route('/')
def error():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    return render_template('index.html')


def hello():
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    app.logger.addHandler(handler)
    app.run()