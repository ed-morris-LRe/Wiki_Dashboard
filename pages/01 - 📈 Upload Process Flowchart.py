# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:03:12 2023

@author: Ed.Morris
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
#import os

# set wd
#rfp_path = r"C:\Users\ed.morris\Documents\Python Scripts\Streamlit SAGE"
#os.chdir(rfp_path)

# Set page configuration
st.set_page_config(page_title='Upload Process Flowchart',page_icon='📈',initial_sidebar_state='expanded')

# Open flowchart pic
flow = Image.open('Upload_Flowchart.jpg')

st.sidebar.success('Select a topic')

st.title('Upload Process Flowchart')
st.markdown("""
            The image below shows the process and questions a user should go through when uploading data to Analyze Re/SAGE. Hopefully this will help visualise the process for a first time upload in an easy to follow manner.
            """)
            
st.image(flow,'Flowchart showing the process to upload data to Analyze Re/SAGE')
