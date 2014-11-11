#!/usr/bin/env python
#coding=utf-8

# imports
import sqlite3
from flask import Flask,render_template,request,url_for,g,redirect
from contextlib import closing

# configuration
DATABASE = 'paper.db'


# application initialize
app = Flask(__name__)
app.config.from_object(__name__)

# database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql',mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# application
@app.route('/')
def hello():
	return render_template('main.html')

@app.route('/<paper>/<alias>')
def generate(paper,alias):
	# 从服务器生成数据
	sql = 'select * from paper where alias="'+alias+'" and papername="'+paper+'" order by number'
	cur = g.db.cursor().execute(sql)
	data = [dict(alias=row[0], papername=row[1], number=row[2], type=row[3], content=row[4], optiona=row[5], optionb=row[6], optionc=row[7], optiond=row[8]) for row in cur.fetchall()]
	return render_template('paper.html',data = data)

@app.route('/add',methods=['POST','GET'])
def add():
	if request.method == 'GET':
		return render_template('newpaper.html')
	else:
		sql = 'insert into paper values(?,?,?,?,?,?,?,?,?,?)'
		data = [request.form['alias'], request.form['papername'], request.form['number'], request.form['type'], request.form['content'], request.form['optiona'], request.form['optionb'], request.form['optionc'], request.form['optiond'], request.form['answer']]
		g.db.cursor().execute(sql,data)
		# 题目信息计入数据库
		g.db.commit()
		# 重定向 新增页面
		# return redirect(url_for('add'))
		return "success"
	
@app.route('/result', methods=['POST'])
def result():
	return 'hehe';

@app.route('/admin')
def admin():
	return render_template('admin.html')

if __name__=="__main__":
	app.debug = True
	app.run()