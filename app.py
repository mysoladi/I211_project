import imp
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

#key for the csv and headers
YOGA_PATH = app.root_path + '/yoga.csv'
YOGA_KEY = ['classname', 'type', 'level', 'date', 'duration', 'trainer', 'description']

# function to read in the csv file
def get_class():
    try:
        with open(YOGA_PATH, 'r', encoding = 'utf-8-sig' ) as csvfile:
            data = csv.DictReader(csvfile)
            yogalist = list(data)
    except Exception as e:
        print(e)
    return yogalist


# route to my normal home index page

@app.route('/')
def index():
    return render_template('index.html')

# creates the name link on my classes page 
@app.route('/classes/')
@app.route('/classes/<class_id>')
def classes(class_id = None):
    classes = get_class()
    return render_template('classes.html', classes =classes, class_id=class_id)


# writes in data to my csv file

def set_class(yoga1):
    try:
        with open(YOGA_PATH, mode='w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=YOGA_KEY)
            writer.writeheader()
            for yoga in yoga1:
                writer.writerow(yoga)

    except Exception as err:
        print(err)

# request the form and iterates through to post my data to my classes page

@app.route('/classes/create', methods =['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        yoga1 = get_class()
        newyoga = {}
    

        newyoga['classname'] = request.form['classname']
        newyoga['type'] = request.form['type']
        newyoga['level'] = request.form['level']
        newyoga['date'] = request.form['date']
        newyoga['duration'] = request.form['duration']
        newyoga['trainer'] = request.form['trainer']
        newyoga['description'] = request.form['description']
        
        yoga1.append(newyoga)
     



        # setting the class to iterate through each dictionary and find each piece of data
        set_class(yoga1)


        return render_template('classes.html')

    else:
        return render_template('addclass.html')