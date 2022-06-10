from keras.models import model_from_json
import numpy as np
import pandas as pd
import streamlit as st
import time
import os
import tensorflow as tf
from tensorflow import keras

subdir = './code'
filename = 'saved_model.pb'
checkpoint_dir = os.path.dirname('./code/saved_model.pb')



st.set_page_config(page_title="Political Party Tweet Classifier App",
                  page_icon="🧊",layout="wide", initial_sidebar_state="expanded"
 )

  

def test_model(loaded_model, tweet):
    print('-----------------------------------')
    class_labels = ['partidoverdemex','PRI_Nacional','AccionNacional','PartidoMorenaMx', 'PRDMexico',
            'MovCiudadanoMX']
    prediction_probs = loaded_model.predict(tweet)
    predicted_label = class_labels[np.argmax(prediction_probs)]
    return predicted_label, prediction_probs
        


@st.cache(allow_output_mutation=True)
def load_model():
    return tf.keras.models.load_model('../saved_model.pb')


    

def description():
    st.write('''
                Hello, welcome to our application: 
             
                Below you can see Our Models Preformance for train and validation set for Loss, Accuracy, Recall, and Precision.
                Go ahead and Test Our Models Preformance on the Sidebar.
             ''')

def main():
    prediction = None
    model = load_model()
    with st.sidebar:
        st.subheader('Test our Model:')
        tweet = st.text_input("Enter tweet from official Twitter account of a Mexican political party:", max_chars = 280)

        if st.button('Run Model'):
            with st.spinner('Wait for it...'):
                if tweet is not None:
                    prediction, animal_perc = test_model(model, tweet)
                    
                    time.sleep(5)     
                    
    st.title('Mexican Tweet Classifier')
    st.write('''---''')
    description()
    st.write('''---''')
    columns()
    if prediction is not None:
        
        st.write(f'The models prediction is...{prediction}')

if __name__ == '__main__':
    app.run(debug=True)