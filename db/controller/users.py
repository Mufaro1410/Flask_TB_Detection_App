from ..dbConfig import db
from ..models.users import User

def createUser(data):
    new_user = User(data)
    db.session.add(new_user)
    user = db.session.commit()
    return user

def getUsers():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return users

def getUser(id):
    user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
    return user

def updateUser(data):
    user = db.get_or_404(User, data.id)
    if user == True:
        updated_user = data
        db.session.add(updated_user)
        user = db.session.commit()
        return user
    return user

def deleteUser(id):
    user = db.get_or_404(User, id)
    if user == True:
        db.session.delete(user)
        res = db.session.commit()
        return res
    return user