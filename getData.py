from flask import Flask,render_template
from flask import request
import pickle
import numpy as np 

getData = Flask(__name__)
@app.route('/getData')

def index():

    return render_template('data.html')


if __name__ == "__main__":
    getData.run(debug=True)