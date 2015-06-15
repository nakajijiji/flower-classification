import os
import json
import datetime
from flask import Flask, jsonify, render_template, request, g, redirect, url_for
from flask.ext.cors import cross_origin

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@cross_origin(headers='Content-Type')
def index():
  name = "world"
  return render_template('index.html', name = name)

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 4000))
  app.run(host='0.0.0.0', port = port, debug = True, threaded = True)
