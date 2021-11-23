from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort

# import ipdb; ipdb.set_trace()

from models import db, Song
from forms import SongForm

bp = Blueprint('songs', __name__)

@bp.route('/songs')
def show_songs():
    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@bp.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    song = Song.query.get_or_404(song_id)
    return render_template('song.html', song=song, playlists=song.playlists)


@bp.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    # import ipdb; ipdb.set_trace()

    form = SongForm()

    if form.validate_on_submit():

        title = form.title.data
        artist = form.artist.data

        new_song = Song(
            title=title,
            artist=artist
        )

        db.session.add(new_song)
        db.session.commit()

        flash(f"New song added: {title} by {artist}")

        return redirect("/songs")

    return render_template("new_song.html", form=form)
