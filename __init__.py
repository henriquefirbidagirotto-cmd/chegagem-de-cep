import os 
from flask import flask
from mvvm.app.views.cep_view import cep_bp


def create_app():
    base_dir = os.path.dirname(os.path.dirname(__file__))

    app = flask(

        __name__,
        template_folder = os.path.join(base_dir,'templates')
    )

    app.register_blueprint(cep_bp)
    return app