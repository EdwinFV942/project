import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://root:@localhost/examen"
    );
    SQLALCHERMY_TRACK_MODIFICATIONS = False