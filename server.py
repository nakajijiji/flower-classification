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

