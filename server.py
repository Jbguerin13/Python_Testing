import json
from flask import Flask,render_template,request,redirect,flash,url_for

#load the clubs and competitions from the json files
def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs

#load the clubs and competitions from the json files
def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__) #create the Flask app
app.secret_key = 'something_special' #used to add a session flash

#load the clubs and competitions
competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    # user can connect from a form (by email)
    return render_template('index.html')

#display welcome page after connextion
@app.route('/show_summary',methods=['POST'])
def show_summary():
    #look for the club in the list of clubs
    for club in clubs:
        if club['email'] == request.form['email']:
            return render_template('welcome.html',club=club,competitions=competitions)
    flash("Wrong credentials, please retry", "error")
    return redirect(url_for('index'))

#display the booking page
@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)

#purchase places
@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    #look for the competition and the club in the list of clubs and competitions
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    #look for the club in the list of clubs
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    #check if there are enough places
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
