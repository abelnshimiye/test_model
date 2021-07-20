import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import joblib
import requests


# from secrets import access_key,secret_access_key

# response = requests.get('https://drive.google.com/drive/folders/1ufzjPwwq2Cb8zDxZskFisl6_gRqA9A7Q?usp=sharing') 

# import urllib3 
# content=urllib3.urlopen("https://drive.google.com/file/d/1yK_upqSxk0VBPbf802nkmJXbO7JOasZ2/view?usp=sharin") 

# import boto3
# import os

# heroku config:set AWS_ACCESS_KEY_ID=AKIAYIJ6NGBHOB2WBN4R AWS_SECRET_ACCESS_KEY=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

# heroku config:set S3_BUCKET_NAME=mamaappmodel

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Type your semptom we will diagnsis you !!!")
st.text("Choose among :")
st.text("Fever")
st.text("Severe Headache")
st.text("Diarhea")
st.text("Fatigue")
st.text("Nausea and Vomiting")
st.text("Muscle Pain")
st.text("Chills")
st.text("Addominal Pain")
st.text("Blurred vision")
st.text("Swollen feet hands and Face")
st.text("Difficulty urinating")
st.text("Pain below the ribs")
st.text("Heartburn")
st.text("Repid heartbeat")
st.text("Vaginal Bleeding at 20 weeks")
st.text("Abdominal cramps")
st.text("Back Pain")
st.text("Clotted discharge from the vaginal")
st.text("Pain on the right side of the abdomen")
st.text("White all your symptoms")

# @st.cache(allow_output_mutation = True)

# def load_model():
#     model = joblib.load('https://mamaappmodel.s3.us-east-2.amazonaws.com/modelupload/bert_qa_custom.joblib')
#     return model

# with st.spinner('loading Model into Memory...'):
#     model = load_model()

text  = st.text_input('Enter yours symptoms here...')

# if text:
#     st.write("Response :")
#     with st.spinner ('Searching for diagnsis...'):
#         prediction = model.predict(text)
#         st.write('answer:{}'.format(prediction[0]))
#         st.write('title:{}'.format(prediction[1]))
#         st.write('paragraph:{}'.format(prediction[2]))
#     st.write("")

