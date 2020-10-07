from app import app
import requests
import json
from app.forms import searchByIdForm
from flask import render_template, redirect, url_for, flash 
from app import config

@app.route('/index', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def index():
    form = searchByIdForm()
    if form.validate_on_submit():
        args = response(form.id.data, form.season.data)
        if args == False:
            return redirect(url_for('index'))
        return render_template('index.html', form=form, args=args)
    return render_template('index.html', form=form)

def response(i, s):
    p = {'i':i, 'season':s, 'apikey':config.apikey}
    resp = requests.get('http://omdbapi.com', params = p)
    if resp.json()['Response'] == 'False':
        flash(resp.json()['Error'])
        return False
    else:
        rating = calcSeasonRating(resp)
        top = highestRated(resp)
        return (rating,top)

def calcSeasonRating(resp):
    count = 0
    tot_rating = 0
    for episode in resp.json()['Episodes']:
        tot_rating += float(episode['imdbRating'])
        count += 1
    season_rating = tot_rating / count
    return round(season_rating,2)

def highestRated(resp):
    r = -1
    t = ''
    num = -1
    for episode in resp.json()['Episodes']:
        if float(episode['imdbRating']) > r:
            t = episode['Title']
            r = float(episode['imdbRating'])
            num = episode['Episode']
    return (r,t,num)
