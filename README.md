# OpenQueue
files for Claypot's OpenQueue project

This repository contains the Python script for Claypot Productions OpenQueue project, specifically the Musicube version of the script as of this time. 
The code was written for Python 3.10 and depends on the json and requests packages.
To get set up to use this script on your own machine and musicube account, you will need to do the following:
1. First, make sure you have created a Musicube account.
2. Go to the Musicube API's web UI and scroll down to find the login endpoint and click to expand it.
3. Click the "try it out" button and edit the request body to include your account email and password and click "execute."
4. If you've done it right, you will be shown a server response below the text box with the request body, which should include a Bearer token. 
5. Copy "Bearer" and the long string of characters following it, and then scroll up to the top of the list of API endpoints and click the "Authorize" button. Paste the Bearer token you copied into the text box and click "authorize." 
6. Paste your Bearer token into the "headers" definition in the Python script, create a file in the same location as the script called "musicube_dump.json" and then run the code to analyze your uploaded tracks.
