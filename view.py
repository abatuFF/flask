from app import app 
from flask import render_template

@app.route('/')
def index():
	f = open('count.txt','r')
	count=int(f.read())
	f.close()

	count += 1

	f=open('count.txt','w')
	f.write(str(count))
	f.close()

	return render_template('app/index.html', count=count)

@app.route('/view')
def third():
	context={
		'languages':'python,css,html,ruby,JS',
	}
	return render_template('app/main.html', **context)

@app.route('/1')
def second():
	posts= ['clown', 'ruck and shmorti', 'anarhi sons']
	context={
	'name':'Danya',
	'age':'500',
	'gender':'man',
	"posts":posts
	}
	return render_template('app/main.html', **context)
