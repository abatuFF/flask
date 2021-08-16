from app import app 
from flask import render_template

@app.route('/')
def index():
	return '<h1>Hello world</h1>'


@app.route('/second')
def second():
	context ={
	'name':'Kazahstan',
	'age':'30',
	'gender':'male',
	}

@app.route('/view')
def third():
	context={
		'languages':'python,css,html,ruby,JS',
	}
	
	return render_template('app/index.html', **context)
