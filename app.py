from flask import Flask, render_template
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
def donation_index():
    return render_template('donations_index.html', donations=donations.find())

if __name__ == '__main__':
    app.run(debug = True)
