from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import TextArea
from wtforms.fields.html5 import DateField
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = 'static/images'

db = SQLAlchemy(app)

class EventForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()], widget=TextArea())
    drivelink = StringField('Drive Link', validators=[DataRequired()])
    image = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __repr__(self):
        return f"EventForm('{self.city}', '{self.country}', {self.description}, {self.date})"


class Event(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False, default="Very beautiful place")
    drivelink = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(50), nullable=False, default='Default Photo.jpg')
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self): 
        return f"Event('{self.city}', '{self.country}', {self.description}, {self.date})"

@app.route('/', methods=['GET','POST'])
def timeline():
    new_events= []
    form = EventForm()
    all_events = Event.query.order_by(Event.date.desc()).all()
    if form.is_submitted():
        filename = None
        try:
            f = form.image.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(UPLOAD_FOLDER,filename))
        except: pass
        new_event = Event(date=form.date.data, image=filename, city=form.city.data, country=form.country.data, description=form.description.data, drivelink= form.drivelink.data)
        db.session.add(new_event)
        db.session.commit()
        return redirect('/')
    return render_template('timeline.html',
     events=all_events, form=form)


@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route("/delete/<int:event_id>", methods=['POST'])
def delete(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect('/')

@app.route("/update/<int:event_id>", methods=['POST'])
def update(event_id):
    form = EventForm()
    event = Event.query.get_or_404(event_id)
    event.city = form.city.data
    event.country = form.country.data
    event.drivelink = form.drivelink.data
    event.description = form.description.data
    event.date = form.date.data

    try:
        f = form.image.data
        filename = secure_filename(f.filename)
        event.image = filename
    except: pass

    db.session.commit()
    return redirect(url_for('timeline'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
