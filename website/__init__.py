from flask import Flask

def create_app():
    app = Flask(__name__) # asi se inicializa flask
    app.config["SECRET_KEY"] = "pedronolaponenienpedo" # key para asegurar cookies y data de session (averiguar al respecto)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app