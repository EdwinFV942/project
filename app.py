from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes.user import user_bp
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    from models.user import User
    
    from routes.user import user_bp
    app.register_blueprint(user_bp)
    
    @app.route('/')
    def home():
        return { "message": "api"}
    
    
    return app;
    
    

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)