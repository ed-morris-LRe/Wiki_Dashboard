# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 08:53:06 2023

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
st.set_page_config(page_title='Demo Upload - Actuarial UI',page_icon='🧭',initial_sidebar_state='expanded')

video_file_1 = open('AnalyzeRe API + Updating Uploads (P1).mp4','rb')
video_bytes_1 = video_file_1.read()
video_file_2 = open('AnalyzeRe API + Updating Uploads (P2).mp4','rb')
video_bytes_2 = video_file_2.read()
video_file_3 = open('AnalyzeRe API + Updating Uploads (P3).mp4','rb')
video_bytes_3 = video_file_3.read()
video_file_4 = open('AnalyzeRe API + Updating Uploads (P4).mp4','rb')
video_bytes_4 = video_file_4.read()
video_file_5 = open('AnalyzeRe API + Updating Uploads (P5).mp4','rb')
video_bytes_5 = video_file_5.read()
video_file_6 = open('AnalyzeRe API + Updating Uploads (P6).mp4','rb')
video_bytes_6 = video_file_6.read()
video_file_7 = open('AnalyzeRe API + Updating Uploads (P7).mp4','rb')
video_bytes_7 = video_file_7.read()

st.sidebar.success('Select a topic')

st.title('AnalyzeRe: API walkthrough')

st.markdown("""
            These videos show how to navigate the AnalyzeRe API to update, edit and replace loss sets in SAGE/AnalyzeRe.
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
st.header('Part 6')
st.video(video_bytes_6)
st.header('Part 7')
st.video(video_bytes_7)