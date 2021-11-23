"""Seed file to make sample data for pets db."""

from models import db, connect_db, Playlist, Song, PlaylistSong
from app import create_app
connect_db(create_app())

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
# PlaylistSong.query.delete()
# Playlist.query.delete()
# Song.query.delete()

# import ipdb; ipdb.set_trace()

# Add pets
p1 = Playlist(name="p1", description="desc 1")
p2 = Playlist(name="p2", description="desc 2")
p3 = Playlist(name="p3", description="desc 3")

s1 = Song(title="t1", artist="a1")
s2 = Song(title="t2", artist="a2")
s3 = Song(title="t3", artist="a3")
s4 = Song(title="t4", artist="a4")
s5 = Song(title="t5", artist="a5")
s6 = Song(title="t6", artist="a6")

# Add new objects to session, so they'll persist
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)
db.session.add(s5)
db.session.add(s6)

# Commit--otherwise, this never gets saved!
db.session.commit()

ps1 = PlaylistSong(playlist_id=p1.id, song_id=s1.id)
ps2 = PlaylistSong(playlist_id=p1.id, song_id=s2.id)
ps3 = PlaylistSong(playlist_id=p2.id, song_id=s3.id)
ps4 = PlaylistSong(playlist_id=p3.id, song_id=s4.id)
ps5 = PlaylistSong(playlist_id=p3.id, song_id=s5.id)
ps6 = PlaylistSong(playlist_id=p3.id, song_id=s6.id)

db.session.add(ps1)
db.session.add(ps2)
db.session.add(ps3)
db.session.add(ps4)
db.session.add(ps5)
db.session.add(ps6)

db.session.commit()
