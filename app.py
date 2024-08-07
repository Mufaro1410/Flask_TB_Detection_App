from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from model import predict_tb

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
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
            return render_template('index.html', filename=filename, result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001)
    app.run(debug=True)
