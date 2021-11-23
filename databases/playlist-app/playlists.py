from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort
from jinja2 import TemplateNotFound

# import ipdb; ipdb.set_trace()

from models import db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, PlaylistForm

bp = Blueprint('playlists', __name__)

@bp.route('/')
def show_index():
    """Homepage: redirect to /playlists."""
    return redirect("/playlists")


@bp.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)
    # return '/playlists'


@bp.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # DONE: get playlist songs
    # DONE: display playlist songs

    playlist = Playlist.query.get_or_404(playlist_id)
    # playlist_songs = PlaylistSong.query.filter_by(playlist_id=playlist_id).all()
    # import ipdb; ipdb.set_trace()
    # song_ids = [song.song_id for song in playlist_songs]
    # songs = Song.query.filter(Song.id.in_(song_ids))
    return render_template("playlist.html", playlist=playlist, songs = playlist.songs)
    # return '/playlists/<int:playlist_id>'


@bp.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    added_songs = [song.id for song in playlist.songs]
    choices = [(song.id, song.title) for song in Song.query.filter(Song.id.not_in(added_songs)).all()]
    form.song.choices = choices

    if form.validate_on_submit():

        # This is one way you could do this ...
        playlist_song = PlaylistSong(song_id=form.song.data, playlist_id=playlist_id)
        db.session.add(playlist_song)

        # Here's another way you could that is slightly more ORM-ish:
        #
        # song = Song.query.get(form.song.data)
        # playlist.songs.append(song)

        # Either way, you have to commit:
        db.session.commit()

        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)
    # return '/playlists/<int:playlist_id>/add-song'


@bp.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        new_playlist = Playlist(
            name = name,
            description = description
        )

        db.session.add(new_playlist)
        db.session.commit()

        flash("New playlist added: {name} - {description}")

        return redirect("/playlists")

    return render_template('new_playlist.html', form=form)
    # return '/playlists/add'
