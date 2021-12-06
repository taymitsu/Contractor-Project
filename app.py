from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.ContractorProject
users = db.users
donations = db.donations

app = Flask(__name__)

#----------------INDEX ALL DONATIONS-----------
@app.route('/')
def donations_index():
    """SHOW ALL DONATIONS"""
    return render_template('donations_index.html', donations=donations.find())

#----------------NEW/CREATE-----------
@app.route('/donations/new')
def donations_new():
    """Create NEW Donation Log"""
    return render_template('donations_new.html')

#----------------DISPLAY ONE-----------
@app.route('/donations/<donation_id>')
def donations_show(donations_id):
    """DISPLAY ONE"""
    donation = donations.find_one({'_id': ObjectId(donation_id)})
    return render_template('donations_show.html', donation=donation)

#----------------SUBMIT ONE-----------
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
    return redirect(url_for('donations_index'))

#----------------EDIT-----------
@app.route('/donations/<donation_id>', methods=['POST'])
def donations_edit(donation_id):
    """Submit Edit"""

#----------------DELETE-----------


#---------------- UPDATE-----------
if __name__ == '__main__':
    app.run(debug = True)
