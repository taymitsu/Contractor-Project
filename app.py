from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.ContractorProject
users = db.users
donations = db.donations

users = [
    { 'username': 'taymitsu', 'password': 'creamofwheatrox'},
    { 'username': 'phiggy', 'password': 'Daximoon'}
]

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
        'name': request.form.get(),
        'amount': request.form.get('donation'),
        'date': request.form.get('date'),
        'notes': request.form.get('notes'),
    }
    print(request.form.to_dict())
    return redirect(url_for('donations_index'))

if __name__ == '__main__':
    app.run(debug = True)
