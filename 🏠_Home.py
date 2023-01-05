# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:26:34 2022

@author: Ed.Morris
"""

### Streamlit dashboard for SAGE User Guide ###

# import modules
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
#import os

# set wd
#rfp_path = r"C:\Users\ed.morris\Documents\Python Scripts\Streamlit SAGE"
#os.chdir(rfp_path)

# Images
sage = Image.open('SAGE_logo.JPG')

# Set page configuration
st.set_page_config(page_title='Home',page_icon=sage,initial_sidebar_state='expanded')

st.sidebar.success('Select a topic')


st.title("""
          SAGE/Actuarial UI User Guide
          """)
          
st.markdown("""
            **Navigating the dashboard:**
            - Use the sidebar to select a topic to read about
            - If the sidebar isn't visible, click the arrow in the top left-hand corner of the screen
            
            **Dashboard Purpose:**
            - To provide new and existing SAGE/Actuarial UI users with knowledge needed to manipulate data for use in SAGE/AnalyzeRe
            - Be an easy-to-access repository for existing and future processes
            """)
