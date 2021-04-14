import numpy as np
import flask
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import pandas as pd
import secrets
from flask_ngrok import run_with_ngrok

secret = secrets.token_urlsafe(32)
app = Flask(__name__)
run_with_ngrok(app) 
app.secret_key = secret


@app.route('/', methods = ['POST', 'GET'])
def home():
	if request.method == 'GET':
		result = request.args.get('getEid')
		if result == "true":
			
			df = pd.read_csv('reviews.csv')
			data = df.sample()
			eid = data['eid'].values

			reviews = []
			reviews.append(data['review_0'].values[0])
			reviews.append(data['review_1'].values[0])
			reviews.append(data['review_2'].values[0])
			reviews.append(data['review_3'].values[0])
			reviews.append(data['review_4'].values[0])
			reviews.append(data['review_5'].values[0])
			reviews.append(data['review_6'].values[0])
			reviews.append(data['review_7'].values[0])


			session['eid'] = eid[0]
			session['reviews'] = reviews
			session['summary'] = ""
			return render_template('index.html')

	elif request.method == 'POST':
		result = request.form.get('eid')
		if result != "":
			data = pd.read_csv('summaries.csv')
			data = data[data.eid == result]
			summary = data['pred'].values
			session['summary'] = summary[0]
			return render_template('index.html')


	session['eid'] = ""
	session['reviews'] = ""
	session['summary'] = ""
	return render_template("index.html")


if __name__ == "__main__":
	app.run()