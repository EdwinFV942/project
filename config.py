import os


class Config:
    SQLARCHERMY_DATABASE = os.getenv(
        "DATABASE_URL", "mysql+pymysql://root:@localhost/examen"
    );
    SQLALCHERMY_TRACK_MODIFICATIONS = False