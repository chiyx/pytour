#! /usr/bin/env python3
# coding = utf-8

import os
from flask import Flask, render_template

rootPath = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, root_path=rootPath)


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/echo/<thing>')
def echo(thing):
    return render_template('echo.html', thing=thing)

app.run(port=9999, debug=True)
