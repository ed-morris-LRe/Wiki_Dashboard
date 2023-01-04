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
#import os

# set wd
#rfp_path = r"C:\Users\ed.morris\Documents\Python Scripts\Streamlit SAGE"
#os.chdir(rfp_path)

# Set page configuration
st.set_page_config(page_title='Installation/Permissions Guide',page_icon='⚙️',initial_sidebar_state='expanded')

# Read in images
ghub_access = Image.open('GitHub_access.jpg')
ghub_pat = Image.open('PAT_creation.jpg')
r_environ_pic = Image.open('Renviron_ss.jpg')

st.sidebar.success('Select a topic')

st.title('Getting Started: R, RStudio, GitHub...')

st.markdown("""
            There are a few things we need to install and set up before we can implement specific/niche updates/edits to uploads in AnalyzeRe/SAGE:
            - R
            - RStudio
            - RTools
            - Access to Lockton Re GitHub to access AnalyzeRe/other specific packages
            """)
            
st.header('Important note!')
st.markdown("If connected to the Lockton network either in office or via PULSE/Cirrus, usually you won't be able to download external applications. To get around this, ensure you suspend/disconnect from the Lockton network and you should be able to proceed with the downloads below without issue.")
            
st.header('Installing R')
st.markdown("""
            R is a programming language with a focus on statistical computing, which most of our tools and infrastructure for the Analytics team is built on/compatible with.
            
            R can be downloaded here: 
            - https://cran.r-project.org/bin/windows/base/
            - Download the latest version available for Windows (R-4.2.2 as at 06/12/2022)
            
            The UI for R on its own is fairly basic and not particularly helpful for viewing datasets or graphically via plots, so we encompass R in an Integrated Development Environment (IDE) called RStudio to improve this functionality...
            """)

st.header('Installing RStudio')
st.markdown("""
            RStudio is an IDE used to improve the UI/GUI of R. It allows us to view datasets and plots in-house, making data analysis and tool development much easier.
            
            RStudio can be downloaded here: 
            - https://posit.co/download/rstudio-desktop/
                        
            Now we have everything we need to run local code, such as the simulation code we have for non-cat lines of business. If we want access to the Lockton/AnalyzeRe packages, we need to set up a GitHub account and get the permissions to acccess these.
            """)

st.header('Installing RTools')
st.markdown("""
            RTools is a collection of software needed to be able to call R from the command line in Windows. This is so we can build and install packages from source code.
            
            RTools can be downloaded here (pick version based on your version of R): 
            - https://cran.r-project.org/bin/windows/Rtools/
            """)
            
st.header('Setting up GitHub account/access')
st.subheader('Creating an account and permissions')
st.markdown("""
            GitHub is an online repository used for software development and version control. This is where Lockton packages are hosted, so we need an account and access to the Lockton-Companies repositories to use these.
            
            Firstly, we need to set up a GitHub account using your Lockton email address. Using the link below, create and verify an account using your work email address ("your.name@lockton.com").
            
            Link to GitHub: 
            - https://github.com/
            
            Once you have a verified account, you will need to email Dave Lytz (DLytz@lockton.com) in the US for him to grant you access to the Lockton-Companies GitHub repositories, as he is the admin. Quote your GitHub account name and Lockton email address when requesting this.
            
            When your GitHub account has been granted access to the Lockton-Companies team, you should be able to click on "Lockton-Companies/lockton-re" in the panel on the left-hand side of your home screen on GitHub (see picture below).
            """)
            
st.image(ghub_access,caption='Lockton-Companies team (red) when access granted')

st.subheader('Setting up your GitHub Personal Access Token (PAT)')
st.markdown("""
            For a full overview of PATs, click the link below, otherwise the below is paraphrased from this link:
                - https://happygitwithr.com/https-pat.html#tldr
            
            1. In the console of your RStudio UI, type "usethis::create_github_token()"
            2. This should open a link to GitHub, where once you log in you should see a page similar to the below screenshot:
            """)
            
st.image(ghub_pat,'Select permissions for the PAT')

st.markdown("""
            3. This area allows you to set the permissions for your GitHub PAT, such as reading, writing, editing etc for the packages you have access to. Recommended scopes to select are "repo", "user" and "workflow" (these should be automatically ticked if you used "usethis:create_github_token()").
            4. IMPORTANT: change expiration of the PAT to "No expiration" - this should mean you will only have to set up a PAT once
            5. Click "Generate token"
            6. Copy the generated PAT (should be a long string of unintelligble letters and numbers), and save this in a txt file somewhere you'll remember, as you can't find it on GitHub again once you close the tab.
            7. Go to your RStudio console and type in "usethis::edit_r_environ()", which should pop up a new script window called ".Renviron"
            8. On the first line of this window, type in "GITHUB_PAT=" and then paste in your GitHub PAT generated earlier
            9. On the second line of this window, type in "ANALYZERE_URL='https://lockton-api.analyzere.net'"
            10. On the third line of this window, type in "ANALYZERE_USERNAME=" followed by your AnalyzeRe username in quotation marks (case sensitive, usually 'firstname.surname')
            11. On the final line of this window, type in "ANALYZERE_PASSWORD=" followed by your AnalyzeRe password in quotation marks
            12. If you don't have a login to AnalyzeRe, contact Dave Lytz or one of the US actuaries who should be able to help set you up with a login.
            
            Once this has been done, it should look like the screenshot below. If so, save it somewhere on your local PC drives near your installations of R/RStudio.
            """)

st.image(r_environ_pic,'Top left panel showing the set up of .Renviron file')

st.markdown("""
            Once all of the above has been downloaded, installed and set up, we need to transfer a couple of files that the installation process currently doesn't place correctly.
            
            Navigate to the local drive: r-miniconda/Library/bin and copy the following files:
            - libcrypto-1_1-x64.dll
            - libssl-1_1-x64.dll
            
            Navigate to the folder r-miniconda/DLLs and paste these files into the folder.
            """)

st.header('Finishing touches...')
st.markdown("""
            Next, we need to install some packages in R to complete the set up process. Run the following commands in the console:
            - install.packages("devtools")
            - devtools::install_github("Lockton-Companies/analyzere")
            
            The second command should access the Lockton-Companies GitHub repository called analyzere, allowing us to use the functions in there. 
            The console should show a message: "using the GitHub PAT from envar GITHUB_PAT" that we set up in our .Renviron file earlier.
            
            Once you have carried out all of the above, try running the library call:
            - library(analyzere)
            
            You should receive the following message in the console:
            - "Registered S3 method overwritten by 'analyzere': method from py_to_r.datetime.datetime reticulate"
            
            Follow this call with:
            - are_set_credentials()
            
            You should receive the following message in the console:
            - "Analyze Re credentials set."
            
            If you get this message, congratulations, you should be able to run uploads via R and access the analyzere and other packages in the Lockton-Companies GitHub such as lorexposure, lorexperience and many more.
            
            If you are having issues, please see the "Setup Troubleshooting" page for some help with common setup problems.
            """)
