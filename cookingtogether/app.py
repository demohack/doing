def create_app(test_config=None):

    # import ipdb; ipdb.set_trace()

    from dotenv import dotenv_values
    settings = dotenv_values("/Users/yu/sb/conf/.env")

    DB_CONFIG = {
        'secret': settings['SECRET'],
        'driver': settings['PGDRIVER'],
        'user': settings['PGUSER'],
        'pw': settings['PGPASSWORD'],
        'db': 'cooking',
        'host': settings['PGHOST'],
        'port': settings['PGPORT'],
    }

    # create and configure the app
    from flask import Flask, redirect
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

    @app.route('/')
    def show_index():
        """Homepage: redirect to /blog."""
        return redirect("/blog")

    from bpblog import bp as blog_bp
    app.register_blueprint(blog_bp)

    from bpauth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from bpevents import bp as events_bp
    app.register_blueprint(events_bp)

    from bprecipes import bp as recipes_bp
    app.register_blueprint(recipes_bp)

    from bpfood import bp as food_bp
    app.register_blueprint(food_bp)

    from bpusers import bp as users_bp
    app.register_blueprint(users_bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
