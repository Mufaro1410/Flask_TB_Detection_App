from db import DB
from models.patients import Patient

def createPatient(data):
    new_user = User(username=data.username, password=data.password)
    db.session.add(new_user)
    db.session.commit()

def getPatients():
    return

def getPatient(id):
    return

def updatePatient(id):
    return

def deletePatient(id):
    return