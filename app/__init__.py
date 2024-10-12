from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración desde 'config.py'
    app.config.from_object('config.Config')

    # Registrar el blueprint (debe existir en views.py)
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
