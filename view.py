from flask import request
from controller import app
from model import Play
from flask import render_template
from decorators import login_required
from google.appengine.api import users


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/login')
@login_required
def login():
	return 'Successfully Logged In!'



@app.route('/log', methods = ['POST'])
@login_required
def log():
	""" Log a play """
	# play = Play(artist = "Artist", album_artist = "Album Artist", album = "Album", title = "Title", user = users.get_current_user())
	play = Play(artist=request.form['artist'],
		album_artist=request.form['album_artist'],
		album=request.form['album'],
		title=request.form['title'],
		user=users.get_current_user())
	play.put()
	print("logged song")
	# flash('Play saved on database.')
	return "Success"


@app.route('/dummy')
@login_required
def dummy():
	""" Debugging page for creating a dummy play """
	play = Play(artist = "Artist", album_artist = "Album Artist", album = "Album", title = "Title", user = users.get_current_user())
	play.put()
	return "Success"	


@app.route('/')
@login_required
def hello():
    """Return a friendly HTTP greeting."""
    plays = filter(lambda p: p.user == users.get_current_user(), Play.all())
    print(plays)
    logout_url = users.create_logout_url('/home')
    logout_url_linktext = 'Logout'
    login_url = users.create_login_url('/home')
    login_url_linktext = 'Login'
    plays = sorted(plays, key=lambda x: x.time)
    return render_template('list_plays.html', plays=plays, logout_url=logout_url, logout_url_linktext=logout_url_linktext, login_url=login_url, login_url_linktext=login_url_linktext)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
