# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/get_results',methods = ['GET', 'POST'])
def get_results():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        form = request.form
        data = model.find_data(form['first_name'], form['month'])
        return render_template('results.html',data=data)

## 1. Write a form to GET user information, the form posts as a method to /results
## 2. Process the data with functions in model.py (user month? birthstone?)
## 3. Return the info to the user
#a. Return to strings (22-24)
#b. Return inside template
#c. Make it nice! (pictures, image tags)