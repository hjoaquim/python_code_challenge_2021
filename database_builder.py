from config import API_KEY
from const import *
from log_config import *
import os
import requests
import json

def create_series_database_imp(series_title = SERIES_TITLE_GOT):
    
    number_of_seasons = get_number_of_seasons(series_title)

    path = DB_PATH + series_title + JSON_SUFFIX

    if os.path.isfile(path) is True:
        os.remove(path)
    
    file = open(path, "a+")
    file.write(json.dumps(get_all_episodes_and_build_comment_section(series_title, number_of_seasons), indent=2))
    file.close()

def get_all_episodes_and_build_comment_section(series_title, number_of_seasons):
    list_of_seasons = []
    i = 1
    while i <= number_of_seasons:
        season_episodes = perform_request(series_title, i)
        
        # Creating the comments stucture
        for episode in season_episodes[EPISODES_KEY]:
            episode.update({COMMENTS_KEY: []})

        list_of_seasons.append(season_episodes)
        i += i

    return list_of_seasons

def get_number_of_seasons(series_title):
    return int(perform_request(series_title)[TOTAL_SEASONS_KEY])

def perform_request(searies_title, season = 1):

    url = API_URL_OMDB.format(searies_title, season, API_KEY)

    payload={}
    headers = {}

    response = requests.request(HTTP_GET, url, headers=headers, data=payload)

    pretty_json = json.loads(response.text)
    logging.info("Response result: " + json.dumps(pretty_json, indent=2))
    return pretty_json