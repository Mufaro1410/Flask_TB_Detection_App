from ..dbConfig import db
from sqlalchemy.orm import Mapped, mapped_column

# class Patient(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(80), unique=True, nullable=False)
#     lastname = db.Column(db.String(80), unique=True, nullable=False)
#     dob = db.Column(db.String(80), unique=True, nullable=False)
#     contact = db.Column(db.String(80), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username
    
class Patient(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    dob: Mapped[int] = mapped_column(nullable=False)
    contact: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return '<Patient %r>' % self.firstname % self.lastname
