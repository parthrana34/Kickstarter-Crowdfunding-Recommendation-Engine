from random import randint
from time import strftime
import csv
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
import pandas as pd
from joblib import load

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    title = TextField('Title:', validators=[validators.required()])
    description = TextField('Description:', validators=[validators.required()])
    goal = TextField('Goal:', validators=[validators.required()])
    updates = TextField('Updates:', validators=[validators.required()])
    duration = TextField('Duration:', validators=[validators.required()])
    level = TextField('Levels:', validators=[validators.required()])
    name = TextField('Name:', validators=[validators.required()])
    category = SelectField('Category:', choices= [('0','Art'),
                                                  ('1','Comics'),
                                                  ('2','Dance'),
                                                  ('3','Design'),
                                                  ('4','Fashion'),
                                                  ('5','Film And Video'),
                                                  ('6','Food'),
                                                  ('7','Games'),
                                                  ('8','Music'),
                                                  ('9','Photography'),
                                                  ('10','Publishing'),
                                                  ('11','Technology'),
                                                  ('12','Theater'),])
    
    subcategory = SelectField('Subcategory:', choices= [('0','Animation'),
                                                        ('1','Art'),
                                                        ('2','Art Book'),
                                                        ('3','Board and Card Games'),
                                                        ('4','Childrens Books'),
                                                        ('5','Classical Music'),
                                                        ('6','Comics'),
                                                        ('7','Conceptual Art'),
                                                        ('8','Crafts'),
                                                        ('9','Dance'),
                                                        ('10','Conceptual Art'),
                                                        ('11','Country and Folk'),
                                                        ('12','Crafts'),
                                                        ('13','Dance'),
                                                        ('14','Design'),
                                                        ('15','Digital Art'),
                                                        ('16','Documentary'),
                                                        ('17','Electronic Music'),
                                                        ('18','Fashion'),
                                                        ('19','Fiction'),
                                                        ('20','Film and Video'),
                                                        ('21','Food'),
                                                        ('22','Games'),
                                                        ('23','Graphic Design'),
                                                        ('24','Hip-Hop'),
                                                        ('25','Illustration'),
                                                        ('26','Indie Rock'),
                                                        ('27','Jazz'),
                                                        ('28','Journalism'),
                                                        ('29','Mixed Media'),
                                                        ('30','Music'),
                                                        ('31','Narrative Film'),
                                                        ('32','Non Fiction'),
                                                        ('33', 'Open Hardware'),
                                                        ('34', 'Open Software'),
                                                        ('35', 'Painting'),
                                                        ('32', 'Performance Art'),
                                                        ('33', 'Periodical'),
                                                        ('34', 'Photography'),
                                                        ('35', 'Poetry'),
                                                        ('36', 'Pop'),
                                                        ('37', 'Product Design'),
                                                        ('38', 'Public Art'),
                                                        ('39', 'Publishing'),
                                                        ('40', 'Rock'),
                                                        ('41', 'Sculpture'),
                                                        ('42', 'Short Film'),
                                                        ('43', 'Technology'),
                                                        ('44', 'Theater'),
                                                        ('45', 'Video Games'),
                                                        ('46', 'Web Series'),
                                                        ('47', 'World Music')])

    category = SelectField('Category:', choices=[('0', 'AK'), 
                                                  ('1', 'AL'), 
                                                  ('2', 'AR'), 
                                                  ('3', 'AZ'), 
                                                  ('4', 'CA'), 
                                                  ('5', 'CO'), 
                                                  ('6', 'CT'), 
                                                  ('7', 'DC'), 
                                                  ('8', 'DE'), 
                                                  ('9', 'FL'), 
                                                  ('10', 'GA'), 
                                                  ('11', 'HI'), 
                                                  ('12', 'IA'), 
                                                  ('13', 'ID'), 
                                                  ('14', 'IL'), 
                                                  ('15', 'IN'), 
                                                  ('16', 'KS'), 
                                                  ('17', 'KY'), 
                                                  ('18', 'LA'), 
                                                  ('19', 'MA'), 
                                                  ('20', 'MD'), 
                                                  ('21', 'ME'), 
                                                  ('22', 'MI'), 
                                                  ('23', 'MN'), 
                                                  ('24', 'MO'), 
                                                  ('25', 'MS'), 
                                                  ('26', 'MT'),
                                                  ('28', 'NC'),
                                                  ('29', 'ND'),
                                                  ('30', 'NE'),
                                                  ('31', 'NH'),
                                                  ('32', 'NJ'),
                                                  ('33', 'NM'),
                                                  ('34', 'NV'),
                                                  ('35', 'NY'),
                                                  ('36', 'OH'),
                                                  ('37', 'OK'),
                                                  ('38', 'OR'),
                                                  ('39', 'PA'),
                                                  ('40', 'RI'),
                                                  ('41', 'SC'),
                                                  ('42', 'SD'),
                                                  ('43', 'TN'),
                                                  ('44', 'TX'),
                                                  ('45', 'UT'),
                                                  ('46', 'VA'),
                                                  ('47', 'VT'),
                                                  ('48', 'WA'),
                                                  ('49', 'WI'),
                                                  ('50', 'WV'),
                                                  ('51', 'WY')])

def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

# def write_to_disk(name, surname, email):
#     data = open('file.log', 'a')
#     timestamp = get_time()
#     data.write('DateStamp={}, Name={}, Surname={}, Email={} \n'.format(timestamp, name, surname, email))
#     data.close()

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    # #print(form.errors)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        subcategory = request.form['subcategory']
        state = request.form['state']
        goal = request.form['goal']
        updates = request.form['updates']
        duration = request.form['duration']
        level = request.form['level']
        name = request.form['name']
        location = request.form['location']
        email = request.form['email']
        if form.validate():
            # write_to_disk(name, surname, email)
            # flash('Hello: {} {}'.format(title, description))
            # flash('Your Category is: {}'.format(category))
            # flash('Your Subcategory is: {}'.format(subcategory))
            # flash('Your Goal is: {}'.format(goal))
            # flash('Your Update is {}'.format(updates))
            # flash('Your Duration is {}'.format(duration))
            # flash('Your Levels is {}'.format(level))
            # flash('Your State is {}'.format(state))
            data = {'updates': [int(updates)], 'subcategory': [int(subcategory)], 'state': [int(state)], 'goal': [float(goal)], 'levels': [int(level)],
                    'duration': [float(duration)]}
            x_tst = pd.DataFrame(data)
            clf = load("FINAL_MODEL.joblib")
            y_pred = clf.predict(x_tst)
            data_csv = [[title, description, category, subcategory, state, goal, updates, duration, level, y_pred]]

            with open('data_storage.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerows(data_csv)
                flash('Csv file written')
                f.close()
            
            if (y_pred == 1):
                flash('Congratulations, Your project might be successful with 80% accuracy')
            elif (y_pred == 0):
                flash('Sorry to inform you but your project might be a failure')
            else:
                flash('No record found...Try Again!')

        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()