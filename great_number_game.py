from flask import Flask, render_template, redirect, session, request
import random # import random module

app = Flask(__name__)
app.secret_key = "unicorns"

@app.route('/')
def home():
	session['number'] = random.randrange(1, 101)
	print "Number:", session['number']
	return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
	session['guess'] = int(request.form['guess'])
	print type(session['guess'])
	number = session['number']
	if session['guess'] == number:
		print "you got it!"
		session['result'] = True
		return render_template("index.html")
	elif session['guess'] > number:
		print "TOO HIGH"
		session['result'] = "Too High!"
	elif session['guess'] < number:
		print "TOO LOW"
		session['result'] = "Too Low!"
	return render_template('index.html', result=session['result'])

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('number')
	session['result'] = False
	return redirect('/')

app.run(debug=True)