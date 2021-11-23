def create_app(test_config=None):

    # import ipdb; ipdb.set_trace()

    from dotenv import dotenv_values
    settings = dotenv_values("/Users/yu/sb/conf/.env")

    DB_CONFIG = {
        'secret': settings['SECRET'],
        'driver': settings['PGDRIVER'],
        'user': settings['PGUSER'],
        'pw': settings['PGPASSWORD'],
        'db': 'playlist-app',
        'host': settings['PGHOST'],
        'port': settings['PGPORT'],
    }

    # create and configure the app
    from flask import Flask
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='{secret}'.format_map(DB_CONFIG),
        SQLALCHEMY_DATABASE_URI='{driver}://{user}:{pw}@{host}:{port}/{db}'.format_map(DB_CONFIG),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
        TESTING=True,
        DEBUG_TB_INTERCEPT_REDIRECTS=False,
    )

    from models import connect_db
    connect_db(app)

    from flask_debugtoolbar import DebugToolbarExtension
    debug = DebugToolbarExtension(app)

    from playlists import bp as playlists_bp
    app.register_blueprint(playlists_bp)
    app.add_url_rule('/', endpoint='index')

    from songs import bp as songs_bp
    app.register_blueprint(songs_bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
