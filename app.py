from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.ContractorProject
users = db.users
donations = db.donations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#----------------HOME----------------
@app.route('/home')
def home():
    return render_template('home.html')

#----------------SHOW----------------
@app.route('/donations')
def donations_index():
    """SHOW Donation Log"""
    return render_template('donations_index.html', donations=donations.find())

#----------------NEW/CREATE-----------
@app.route('/donations/new')
def donations_new():
    """Create NEW Donation Log"""
    return render_template('donations_new.html')

#SUBMIT NEW 
@app.route('/donations', methods=['POST'])
def donations_submit():
    """Submit Donation Record"""
    donation = {
        'charity': request.form.get('charity'),
        'date': request.form.get('date'),
        'amount': request.form.get('amount'),
        'notes': request.form.get('notes'),
    }
    donations.insert_one(donation)
    #return redirect(url_for('donations_index'))

if __name__ == '__main__':
    app.run(debug = True)
