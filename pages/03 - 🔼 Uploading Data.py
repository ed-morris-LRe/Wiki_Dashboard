# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:28:51 2022

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
st.set_page_config(page_title='Uploading Data',page_icon='🔼',initial_sidebar_state='expanded')

api_converter = Image.open('API_converter.JPG')
are_api = Image.open('ARe_API.JPG')
padded_ec = Image.open('Padded_event_catalogue.JPG')
aud = Image.open('AUD_upload.JPG')


r_script = open('test.txt','r')
file = r_script.read()
r_script.close()

st.sidebar.success('Select a topic')

st.title('Uploading Data to AnalyzeRe/SAGE')

st.write("""
            There are a few methods to upload data to AnalyzeRe/SAGE. The circumstance of the upload may change the method required to upload the data.
            
            **Available tools to upload data:**
            - Actuarial UI
            - R scripts
            """)

selectbox_selections = tuple(['First/new upload','Updating an existing upload','Multicurrency uploads'])
upload_type = st.selectbox('Select an upload type:', selectbox_selections)

if upload_type == 'First/new upload':
    st.title('First/new upload')
    st.write("""
                If we are uploading to AnalyzeRe for the first time, we have a few options when it comes to uploading. We can use either the Actuarial UI (quickest, easiest, simplest), or we can use the "upload-to-are.R" R script.
                - Would recommend using the UI for uploads where possible
                **Benefits of using the UI for uploading data:**
                - Intuitive UI
                - Produces the necessary IDs for connecting the upload to SAGE automatically
                - Eventually the UI will be able to integrate uploads directly into SAGE
                - Doesn't require any permissions to the Lockton GitHub packages, or the setting up R/RStudio on your laptop
                
                **Steps:**
                - Access the Actuarial UI: https://loreact.azurewebsites.net
                - Select a user to login as and click Login (currently this step doesn't matter, in future it will be integrated into everyone's SAGE user account)
                - At the bottom of the sidebar, click Upload to SAGE
                """)

    st.image(Image.open('Actuarial_UI_Upload.jpg'))
    
    st.write("""
             - Under "Choose CSV File", click "Browse..." and click the YELT to upload
                 - There will be a progress bar, once this completes you should see the head of the file at the bottom of the page
             - Beneath these, update the information below for "Client", "Year", "Program", "Description", "Trial Count", "YELT Breakout Level", and optionally any "Filters"
                 - For "Trial Count", set this equal to the maximum trialID in the data
                 - For "YELT Breakout Level", set this to how you want the loss set to be split from the YELT, to appear in SAGE/AnalyzeRe
                     - For example, we would typically put "line","loss_type" for non-cat uploads
                 - "Filter" is an optional argument if you wanted to specify certain ways to filter the data in SAGE
                     - This defaults to "loss_type"
            Once these steps have been carried out, we can click "Upload to AnalyzeRe", to begin the upload.
            
            Here, a progress bar with a short description of each step of the upload will appear in the bottom-right corner of the screen. If the upload completes successfully, a pop-up will appear, displaying various portfolio IDs required to connect SAGE to the upload in AnalyzeRe. There is also an option to download these IDs (highly recommended).
             """)

    st.header('Connecting SAGE to ARe: Admin Dashboard')
    st.markdown("""
            Once you have the IDs for the upload, head across to SAGE and click on the admin dashboard in the panel on the left. Here, we will either need to create a new client, year, programme or structure to put our upload in. Here are the steps from scratch (skip where appropriate for your upload):
            - Establish whether you need to create a new client space in SAGE, or whether we just need to add a year, programme or just a new structure to an existing client
            
            Assuming we have an client space for our upload but need a new programme (often the case):
            1. Firstly search the client name in the "Companies" tab
            2. Take the ID number shown in the first column of your client, click the "Years" tab and search this number in there
            3. Find the row that matches the number you searched in the "Carrier ID" column, and take the ID in the first column from the row that matches the correct Year you want to upload to
            4. Go to the "Programs" tab, click "Add New" and enter the ID found in step 3 in the "Carrier Year ID" section
            5. Name your programme in the "Name" section, add a description in the "Description" section, click "Add"
            6. You should see a brief message, saying "Program ID X created successfully"
            7. Go to the "Structures" tab, click "Add New" and enter the "X" number shown (alternatively scroll to the bottom of the suggestions list, as this is in chronological order of creation)
            8. Enter a name for the structure you want to create in the "Label" section (usually use "Base" for a first upload), and enter a description in the "Program Type" section
            9. Enter all the corresponding IDs we downloaded from the Actuarial UI from our upload into the correct sections
            10. Click "Add", refresh your webpage/SAGE and navigate to the Client -> Year -> Program -> Structure we designated above, and you should see your upload!
            
            See the page titled "Demo Upload - Actuarial UI" for a full video demonstration of a non-cat upload via the UI.
            """)
                
if upload_type == 'Updating an existing upload':
    st.header('Updating an existing upload')
    st.markdown("""
                If we are updating an existing upload, there are two situations in which we may find ourselves:
                1. Replacing existing loss sets in an existing upload
                2. Adding new loss sets to an existing upload
                """)
    st.header('1. Replacing existing loss sets')
    st.markdown("""
                If we want to delete an existing loss set and replace it with a new one, this is relatively simple (but still requires the use of an R script).
                
                Firstly, need the "update-to-are.R" script. This is very similar to the "upload-to-are.R" script, however we have the option to specify the analysis profile to upload to.
                We require the loss sets in the same format as usual (a YELT). The only difference is the allocation of eventids. The eventids MUST correspond to the eventids of the loss sets we originally uploaded. Check the original upload file to see these. If we don't match the eventids, Analyze Re won't allow us to add loss sets to the analysis profile, as the event catalogue is static from the original upload.
                
                In the "update-to-are.R" script, you will need to specify:
                - If we want to add a suffix to the new loss sets to show they have been re-uploaded (e.g. re-modelled loss sets), we can specify this around line 15/16 in the code
                - The analysis profile ID we are uploading to
                - Client information, e.g. client name, program name, year
                
                The output of this script is a csv file containing details for each loss set uploaded, including the line, loss_type, premium, excpense ratio and a couple of layer IDs. We want to convert these IDs to a JSON format so we can paste them into the AnalyzeRe API to update our original upload. We have an excel template that does this for us:
                - Paste the output of the "update-to-are.R script into the API_converter.xlsx file
                - Drag the formula down if required
                - Ensure the final curly bracket is not followed by a comma
                - Copy the text in cell E19 down to the bottom, ensuring all loss set IDs have been picked up, save somewhere in a .txt file for reference
                """)
    st.image(api_converter,'Pasted output of "upload-to-are.R" script at the top, API code in red')
    
    st.header('Analyze Re API')
    st.markdown("""
                Once we have the JSON formatted API code for our loss sets, we can now head across to the Analyze Re API:
                - https://lockton-api.analyzere.net/
                
                To find our existing upload, we need the ParentGrossPortfolioID, which can be found as the final ID in the URL of the design screen of the existing upload in SAGE, via the AnalyzeRe Excel add-in, or from the Actuarial UI ID output.
                
                From the link provided in the bullet point above, add the following to the URL:
                - "/portfolios/ParentGrossPortfolioID"
                
                Which should look like this (example):
                - https://lockton-api.analyzere.net/portfolios/b683c76d-f28d-4e61-8090-7b91b3f65bd3
                
                Here, each "sink" contains a loss set (if in SAGE, the loss sets should appear in order from top to bottom as listed in the Design screen). 
                """)
    st.image(are_api,'An example of the loss set listing via the Analyze Re API')
    
    st.markdown("""
                If we scroll to the bottom of the page, we can find all of the loss sets as seen above but in a text editor. This is where we make edits to the loss set listing. 
                
                Firstly, we need to identify which loss sets we are replacing that need to be deleted. We can do this by clicking each of the links above, scrolling to the bottom and checking the name of each loss set.
                - When you find a loss set you want to replace, go to the text editor of the original page and take a cut of the loss set "sink"
                - Save this somewhere (in case we want this reinstating at a later date)
                - Repeat this until you have removed all loss sets to be replaced 
                - Now, add a comma after the final loss set sink in the text editor, and paste in the JSON formatted API code we generated in the converter earlier
                - Click "PUT", which saves the changes
                
                The page should refresh, and you should now see the loss set "sinks" you added at the bottom. If you refresh the SAGE webpage, you should now find your new loss sets and the old ones should no longer be there.
                """)
    st.header('WARNING!')
    st.markdown("""
                When removing a loss set from SAGE, it is imperative that the loss set is unselected from all structures in the analysis profile, and is ungrouped from any groups and any shared limits. If you don't do this, the loss set will disappear as expected, but the premium, expense and losses will still feed into the portfolio level numbers. 
                
                If you notice phantom numbers in SAGE that line up with an old loss set, reinstate the loss set in the API using the "sink" we cut out above and deselect it appropriately in SAGE before trying to remove it again.
                """)
                
    st.header('2. Adding additional loss sets')
    st.markdown("""
                The other scenario we might face is adding an additional loss set to an existing upload. We can split this into two further scenarios:
                1. Adding alternative views of existing loss set (e.g. uplifts, reductions etc)
                2. Adding entirely new loss sets to an existing upload (e.g. needed modelling in SAGE for initial analysis, have data to model other LOBs at later date)
                
                We will tackle scenario 1 first, then scenario 2.
                """)
    st.header('2.1: Adding alternative view of existing loss set')
    st.markdown("""
                To do this, we can share the eventid of the existing loss set. This scenario requires less (not zero) pro-active planning, as we can borrow the existing eventid for this loss set in the event catalogue.
                
                The key thing we must constrain in the YELT of the original upload is the "day" value. These numbers must range between 0-365, so if we keep the day values for the original upload between 0-100, you can get roughly another 3 updates to loss sets (100-200, 200-300, 300-365). Then in our alternative view of this loss set, we ensure our day values don't overlap with the original upload by constraining these to values between 100-200 (these bins can be manually adjusted, these numbers are just an example).
                
                By maintaining separate day values, we ensure the losses for the original and alternative loss set don't clash. We run the "update-to-are.R" script as mentioned in the replacement of existing loss sets, follow the process through to the Analyze Re API but instead of cutting the "sink" of the loss set in the original upload, we simply add our new JSON formatted API code for our alternate loss set(s) to the bottom of the text editor, and click "PUT".
                """)
    
    st.header('2.2: Adding entirely new loss set')
    st.markdown("""
                This scenario requires slightly more preparation, however to save time you can use a similar eventid-sharing method as above if you don't ever need to turn on an existing loss set and a new loss set in the same structure. However, most of the time this won't be the case and we will require full functionality of the loss set.
                
                To do this, we must pad the event catalogue in our original upload. The video in the "Navigating the AnalyzeRe API" page demonstrates this process briefly, for a visual runthrough.
                
                We need to pad a few extra lines (4 for each loss set, 2x attr, 2x large), with extra lob_id's and extra corresponding eventids (generally lob_id x 10 for attr and lob_id x 10+1 for large). We can pad as many as we like, if you know exactly how many extra loss sets you will need to add retrospectively, create this number of padded lines/eventids.
                
                Once you have done this, we again follow the same "update-to-are.R" script upload process, again adding the loss set "sink" to the bottom of the text editor in the AnalayzeRe API rather than replacing any "sinks".
                """)
    
    st.image(padded_ec,'Example of padded event catalogue in YELT')
    
    st.header('Code/converter')
    st.markdown("""
                The 'update-to-are.R' script and API code converter can be found here:
                - M:/Administration/Actuarial/R + AnalyzeRe/2. R Analyze Re upload code/Update Existing Upload
                """)

if upload_type == 'Multicurrency uploads':
    st.header('Multicurrency Uploads')
    st.markdown("""
                Sometimes we will want to upload to SAGE with multiple currencies in our structures. To do this, we will require the use of R scripts, the "upload-to-are.R" script you might be familiar with already, and the "create-structures.R" script, which you might be less familiar with.
                
                To begin with, we want the usual YELT format for our loss data fed into the "upload-to-are.R" script as usual, which will provide us with an analysis profile ID and an RDS file, both of which feed into the "create-structures.R" script as inputs.
                
                It is in the "upload-to-are.R" script that we can specify an FX table if we want to use exchange rates that aren't set as default in SAGE. On line 209 we read in a csv file containing a full list of currencies that we can specify our upload to, in which we can customise the FX rates. This is uploaded as the exchange rate profile for this specific upload, and won't impact existing or future uploads unless specified upon upload again.
                
                It is in the "create-structures.R" script that we make edits for the relevant currency. In the "create_sage_portfolios()" function, on line 32 we specify the currency we want to upload in. Some examples of the currencies we can specify are as follows:
                - EUR = Euro
                - USD = US Dollar
                - AUD = Australian Dollar
                - CAD = Canadian Dollar
                - GBP = British Pound
                
                A full list of specific currencies can be found in the FXRates.csv file found in the link at the bottom of this section.
                
                When running the "create-structures.R" script, we need to specify the usual things, such as client name, year, program name etc. We also need to ensure the names of the output files from the upload script match the file names we are trying to read in in the current script.
                
                The output of this script is the IDs we get when uploading via the UI, enabling us to connect SAGE to Analyze Re.
                
                We then take these IDs to the SAGE Admin Dashboard as discussed in the First Upload section, add these to a new structure and we should see our upload in the designated currency we chose.
                """)
                
    st.image(aud,'Example of Australian Dollar Upload in SAGE on y-axis')
    
    st.header('Code/FX Rates')
    st.markdown("""
                The 'upload-to-are.R' and 'create-structures.R' scripts, along with FX Rates table can be found here:
                - M:/Administration/Actuarial/R + AnalyzeRe/2. R Analyze Re upload code/Multicurrency Upload
                """)
