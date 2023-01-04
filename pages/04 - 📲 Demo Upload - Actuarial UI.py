# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:42:05 2022

@author: Ed.Morris
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import os

# set wd
rfp_path = r"C:\Users\ed.morris\Documents\Python Scripts\Streamlit SAGE"
os.chdir(rfp_path)

# Set page configuration
st.set_page_config(page_title='Demo Upload - Actuarial UI',page_icon='📲',initial_sidebar_state='expanded')

video_file_1 = open('Actuarial UI - SAGE Upload Demo (P1).mp4','rb')
video_bytes_1 = video_file_1.read()
video_file_2 = open('Actuarial UI - SAGE Upload Demo (P2).mp4','rb')
video_bytes_2 = video_file_2.read()
video_file_3 = open('Actuarial UI - SAGE Upload Demo (P5).mp4','rb')
video_bytes_3 = video_file_3.read()
video_file_4 = open('Actuarial UI - SAGE Upload Demo (P4).mp4','rb')
video_bytes_4 = video_file_4.read()
video_file_5 = open('Actuarial UI - SAGE Upload Demo (P5).mp4','rb')
video_bytes_5 = video_file_5.read()

st.sidebar.success('Select a topic')

st.title('Data Upload: Actuarial UI Demo')

st.markdown("""
            These videos show a demo of the Actuarial UI being used to upload a dummy non-cat dataset to AnalyzeRe.
            """)

st.header('Part 1')
st.video(video_bytes_1)
st.header('Part 2')
st.video(video_bytes_2)
st.header('Part 3')
st.video(video_bytes_3)
st.header('Part 4')
st.video(video_bytes_4)
st.header('Part 5')
st.video(video_bytes_5)