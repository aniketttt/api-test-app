from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import File
import os
from datetime import datetime

@app.route('/')
def index():
    files = File.query.all()
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        file_type = os.path.splitext(filename)[1]
        new_file = File(name=filename, file_type=file_type, upload_date=datetime.now())
        db.session.add(new_file)
        db.session.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
