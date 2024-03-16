import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

from models import db, Person_info

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/images'  # Use forward slashes for paths

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    Person_infos = Person_info.query.all()
    return render_template('index.html', Person_infos=Person_infos)

@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        address = request.form['address']
        mobile_number = request.form['mobile_number']
        email = request.form['email']
        image = request.files['image']
        
        # Save the image file
        if image:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(filename)
            image_path = os.path.relpath(filename, app.static_folder)

            # Normalize image path (replace backslashes with forward slashes)
            image_path = image_path.replace('\\', '/')
            
            # Insert Person_info data into the database
            new_Person_info = Person_info(name=name, address=address, mobile_number=mobile_number, email=email, image_path=image_path)
            db.session.add(new_Person_info)
            db.session.commit()
        
        return redirect(url_for('home'))
    return render_template('add_person.html')

if __name__ == '__main__':
    app.run(debug=True)
