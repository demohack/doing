"""Models for Playlist app."""

# import ipdb; ipdb.set_trace()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist"""

    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)

    songs = db.relationship('Song', secondary="playlist_song")

    def __repr__(s) -> str:
        return f"<p {s.id} {s.name}>"


class Song(db.Model):
    """Song"""

    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    artist = db.Column(db.Text)

    playlists = db.relationship('Playlist', secondary="playlist_song")

    def __repr__(s) -> str:
        return f"<s {s.id} {s.title} {s.artist}>"


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song"""

    __tablename__ = 'playlist_song'

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), primary_key = True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key = True)

    def __repr__(s) -> str:
        return f"<ps {s.playlist_id} {s.song_id}>"


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)
