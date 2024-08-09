# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydb.db'
    UPLOAD_FOLDER = './static/images'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
