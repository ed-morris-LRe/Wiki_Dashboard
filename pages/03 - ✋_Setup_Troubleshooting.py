# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:02:05 2022
@author: ed.morris
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st

# Set page configuration
st.set_page_config(page_title='Setup Troubleshooting',page_icon='✋',initial_sidebar_state='expanded')

st.title('Setup Troubleshooting Guide')
st.markdown("""
            This page will contain some basic guidance and things to try when facing common issues upon setup.
            """)

st.header('Analyze Re credentials')
st.markdown("""
            Sometimes when setting our Analyze Re credentials via "are_set_credentials()", R won't recognise them from our .Renviron file. It is possible to create a .Renviron file that isn't being called when setting credentials. To ensure R is looking at the correct .Renviron file, call the following command in the RStudio console:
            - usethis::edit_r_environ()
            - If the .Renviron file it opens is empty, we know it is looking at the wrong .Renviron file for our Analyze Re credentials
            - In this new, empty .Renviron file, set up your GitHub PAT and Analyze Re credentials as explained in the original guide, and ensure you save this .Renviron file once complete
            - Close the .Renviron file, then call the command above again, and you should see it open the file we just saved
            """)

st.header('Analyze Re credentials: Miniconda error')
st.markdown("""
            Sometimes when running the "are_set_credentials()" command, you will get a vague error where it references and attempts to install miniconda. The fix for this is:
            - The transfer of the .dll files to the correct folder
            - Ensure these files have been transferred as specified as these are the cause of this error
            - The details of this process can be found on the installation guide, at the end of the section called "Setting up your GitHub Personal Access Token (PAT)"
            """)

st.header('Uploading via Actuarial UI: UI Upload fails')
st.markdown("""
            Sometimes our upload to the UI itself will fail (before trying to upload to Analyze Re). A couple of things to try to remedy this are:
            - Check the upload file is a csv or rds
            - Ensure column headings are spelt correctly, e.g. 'expense_ratio' rather than 'expense ratio'
            - Ensure the uploaded file has all columns (particularly the numeric columns) formatted as general, ensuring that numbers don't contain commas (the UI can't read numbers in this format)
            - Ensure there are no blanks in any cells, specify 0s if you mean 0s rather than blanks
            """)

st.header('Uploading via Actuarial UI: Analyze Re Upload fails')
st.markdown("""
            Sometimes the data will upload to the UI without issue, but the screen might grey out and the progress bar disappear when uploading to Analyze Re. A couple of things to try to remedy this are:
            - The UI times out after so long, so ensure wifi speeds are fast when uploading larger files (apparently the time-out period cannot be increased)
            - Ensure the upload contains a column called "loss_type", specifying "attr", "large" or "cat", since the default filter is set to be this column and will error if it isn't in the upload file
            - Carry out checks to ensure there is no overlapping of eventids across lines of business/perils (usually in cat simulation code called EventCheck)
            """)

