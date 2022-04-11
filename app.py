import imp
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def classes():
    return render_template('classes.html')

@app.route('/')
def addclass():
    return render_template('addclass.html')