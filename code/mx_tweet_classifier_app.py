from keras.models import model_from_json
import numpy as np
import pandas as pd
import streamlit as st
import time
import os
import tensorflow as tf
from tensorflow import keras
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Bienvenidos!  Welcome!!'

@app.route('/sk-learn_model')
def cvec_mnb_page():
    return '''
    <html>
        <body>
        <h1> Scikit-Learn </h1>
        <p> This is a header for testing my best model created by scikit-learn </p>
        </body>
    </html>
    '''

# custom 404 message
@app.errorhandler(404)
def page_not_found(error):
    return "URL does not exist.  Please check for typos and try again."

if __name__ == '__main__':
    app.run(debug=True)