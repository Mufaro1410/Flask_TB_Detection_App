# app/__init__.py
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
# from flask_sqlalchemy import SQLAlchemy
import os
from model import predict_tb

# db = SQLAlchemy()

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['UPLOAD_FOLDER'] = './static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}


# with app.app_context():
#     db.create_all()


os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
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
    app.run(port=5001)
    app.run(debug=True)
