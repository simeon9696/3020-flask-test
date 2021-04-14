import numpy as np
import flask
from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)
EID = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/summary",methods=['POST'])
def get_summary():
	data = pd.read_csv('summaries.csv')
	
	data = data[data.eid != EID]
	
	summary = data['pred'].values
	return render_template('index.html', summary_text='{}'.format(summary))

""" @app.route("/reviews",methods=['POST'])
def results():
	df = pd.read_csv('reviews.csv')
	data = df.sample()
	
	EID = data['eid'].values
	reviews = ""
	r1 = data['review_0'].values
	r2 = data['review_1'].values
	r3 = data['review_2'].values
	r4 = data['review_3'].values
	r5 = data['review_4'].values
	r6 = data['review_5'].values
	r7 = data['review_6'].values
	r8 = data['review_7'].values
	
	reviews = r1 + "\n" + r2 + "\n" + r3 + "\n" + r4 + "\n" + r5 + "\n" + r6 + "\n" + r7 + "\n" + r8
	
	return render_template('index.html', review_text='{}'.format(reviews)) """

if __name__ == "__main__":
    app.run(debug=True)