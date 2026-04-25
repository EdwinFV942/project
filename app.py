from flask import Flask
from flask_migrate import Migrate
from config import Config
from models.user import db  # 👈 IMPORTANTE: importar db desde models

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar db
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelo (para registrarlo)
    from models.user import User

    # Blueprints
    from routes.user import user_bp
    app.register_blueprint(user_bp)

    @app.route('/')
    def home():
        return {"message": "api"}

    return app


app = create_app()

# 🔥 Crear tablas (para pruebas)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)