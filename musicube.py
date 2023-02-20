import json
import requests

API_ENDPOINT_FILES = "https://api.musicu.be/api/v1/user/files"

#the bearer token in the headers below is included for all requests to authorize them with the API.
#to set up this code on your own musicube account, go to the musicube API web UI and run the login endpoint through the
#web UI using your account login credentials in the request body. If you did it right, it will give you a bearer token in the
#response. Then, click on the "authorize" button above the list of API endpoints and input your bearer token (making
#sure to include the word "Bearer" at the beginning). Once authorized through the web UI, substitute your token
#into the headers definition below and run the code.
headers = {'accept': 'application/json',
           'Authorization': 'Your Bearer Token Here'
           }

musicube_file_info = requests.get(url=API_ENDPOINT_FILES, headers=headers)
response = musicube_file_info.json()
max_track_index = len(response) - 1
API_ENDPOINT_FEATURES = "https://api.musicu.be/api/v1/public/recording/"
isrcs = []
index_1 = 0
#the following while loop constructs the URL needed for the musical features API endpoint
#and it also pulls out the isrc for each track and adds it back into response as a top-level key to make sorting easier
while index_1 <= max_track_index:
    isrc = {"isrc" : response[index_1]["recording"]["isrc"]}
    isrcs.append(response[index_1]["recording"]["isrc"])
    response[index_1].update(isrc)
    API_ENDPOINT_FEATURES += isrcs[index_1]
    API_ENDPOINT_FEATURES += "%2C"
    index_1 += 1

API_ENDPOINT_FEATURES += "/musicalFeatures?page=0&size=20"
#the line below sorts response by the value of the isrc key added in the while loop above, making the order of data
#blocks in the file info response match that of the musical features response
response.sort(key=lambda x: x["isrc"])
musical_features = requests.get(url=API_ENDPOINT_FEATURES, headers=headers)
features = musical_features.json()
#the following indexer and while loop add the track title into each track's data block in features
index_2 = 0
while index_2 <= max_track_index:
    y = {"name" : response[index_2]["name"]}
    features[index_2].update(y)
    index_2 += 1

#format features and turn it into a json string, then write that to a file
features_string = json.dumps(features, indent=4)
with open('musicube_dump.json', 'w') as outfile:
    outfile.write(features_string)
