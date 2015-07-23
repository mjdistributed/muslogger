from google.appengine.ext import db

class Play(db.Model):
	artist = db.StringProperty(required = True)
	album_artist = db.StringProperty(required = True)
	album = db.StringProperty(required = True)
	title = db.StringProperty(required = True)
	time = db.DateTimeProperty(auto_now_add = True)
	user = db.UserProperty(required = True)