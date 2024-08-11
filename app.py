# app/__init__.py
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os

from model import predict_tb

from db.dbConfig import db
from db.models.users import User
from db.models.patients import Patient


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskDB.db'
app.config['UPLOAD_FOLDER'] = './static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}


db.init_app(app)

with app.app_context():
    db.create_all()


os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    if request.method == 'POST':
        # return redirect(request.url)
        # return render_template("index.html")
        return "POST request received!"
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     print(request.url)
    #     return redirect(request.url)
    return render_template('login.html')

@app.route("/user", methods=['GET', 'POST'])
def user():
    usersList = []
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = { 'username': username, 'password': password }
        db.session.add(user)
        new_user = db.session.commit()
        usersList.append(new_user)
        return render_template("users.html", users=usersList)
    users = db.session.execute(db.select(User).order_by(User.id)).scalars()
    usersList.append(users)
    return render_template("users.html", users=users)

# @app.route("/user/<int:id>")
# def user_id(id):
#     user = db.get_or_404(User, id)
#     return render_template("user.html", user=user)

patientsList = []
@app.route("/patient")
def patient():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dob = request.form['dob']
        contact = request.form['contact']
        patient = { 'firstname': firstname, 'lastname': lastname, 'dob': dob, 'contact': contact }
        db.session.add(patient)
        new_patient = db.session.commit()
        patientsList.append(new_patient)
        return render_template("patenpatients.html",patients=patientsList)
    patients = db.session.execute(db.select(Patient).order_by(Patient.id)).scalars()
    patientsList.append(patients)
    return render_template("patients.html", patients=patients)

@app.route("/patient/<int:id>")
def patient_id(id):
    patient = db.get_or_404(Patient, id)
    return render_template("patient.html", patient=patient)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = predict_tb(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return render_template('index.html', filename=filename, result=result)
            return render_template("result.html", pred=result['predicted'], filename=filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5002, debug=True)
