from ..dbConfig import db
from sqlalchemy.orm import Mapped, mapped_column

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    passwors: Mapped[str]

    def __repr__(self):
        return '<User %r>' % self.username