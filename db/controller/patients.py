from db import db
from models.patients import Patient

def createPatient(data):
    new_patient = Patient(firstname=data.firstname, lastname=data.lastname, dob=data.dob, contact=data.contact)
    db.session.add(new_patient)
    db.session.commit()

def getPatients():
    return

def getPatient(id):
    return

def updatePatient(id):
    return

def deletePatient(id):
    return