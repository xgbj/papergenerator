#!/usr/bin/env python
#coding=utf-8

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello,world'

@app.route('/<paper>/<alias>')
def generate(paper,alias):


if __name__=="__main__":
	app.debug = True
	app.run()