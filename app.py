from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import datetime


client = MongoClient()
db = client.ContractorProject

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

#----------------SUBMIT(Submit New/above)-----------
@app.route('/donations', methods=['POST'])
def donations_submit():
    """Submit NEW Donation Record"""
    donation = {
        'charity': request.form.get('charity'),
        'date': datetime.datetime.now(),
        'amount': request.form.get('amount'),
        'notes': request.form.get('notes'),
    }
    donations.insert_one(donation)
    return redirect(url_for('donations_index'))

#----------------DISPLAY ONE-----------
@app.route('/donations/<donation_id>')
def donations_show(donation_id):
    """DISPLAY ONE"""
    donation = donations.find_one({'_id': ObjectId(donation_id)})
    return render_template('donations_show.html', donation=donation)

#----------------DELETE-----------
@app.route('/donations/<donation_id>/delete', methods=['POST'])
def donations_delete(donation_id):
    """Delete ONE Donation Log"""
    donations.delete_one({'_id': ObjectId(donation_id)})
    return redirect(url_for('donations_index'))

#----------------EDIT-----------
@app.route('/donations/<donation_id>/edit')
def donations_edit(donation_id):
    """Submit Edit"""
    donation = donations.find_one({'id': ObjectId(donation_id)})
    #redirect to Show/DISPLAY ONE 
    return render_template('donations_show.html', donation=donation, title='Edit Donation Record')

#---------------- UPDATE(Submit Edit/above)-----------
@app.route('donations/<donation_id>/', methods=['POST'])
def donations_update(donation_id):
    """Submit Edit"""
    updated_donation = {
        'charity': request.form.get('charity'),
        'date': datetime.datetime.now(),
        'amount': request.form.get('amount'),
        'notes': request.form.get('notes'),
    }
    #Redirect to newly updated
    donations.update_one(
        {'id': ObjectId(donation_id)},
        {'$set': updated_donation})
    #redirect to Show/DISPLAY ONE 
    return redirect(url_for('donations_show', donation_id=donation_id))

if __name__ == '__main__':
    app.run(debug = True)
