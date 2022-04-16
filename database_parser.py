from turtle import update
from const import *
from log_config import *
import os
import json
from fastapi import FastAPI, HTTPException

def get_database(series_title):
    
    path = DB_PATH + series_title + JSON_SUFFIX
    
    if os.path.isfile(path) is False:
        raise HTTPException(status_code=HTTP_404, detail=ERROR_MSG_DB_NOT_FOUND)

    file = open(path, "r")
    data = json.load(file)
    file.close()

    return data

def update_database(series_title, data):
    path = DB_PATH + series_title + JSON_SUFFIX
    f = open(path, "w")
    f.write(json.dumps(data, indent=2))
    f.close()

def get_episodes_per_season_imp(season, series_title):

    seasons = get_database(series_title)
    return get_season_episodes(seasons, season)

def get_season_episodes(seasons, season):
    for s in seasons:
        if int(s[SEASON_KEY]) == season:
            return s[EPISODES_KEY]
    
    raise HTTPException(status_code=HTTP_404, detail=ERROR_MSG_SEASON)

def get_episode_details_imp(id, series_title):
    seasons = get_database(series_title)
    return get_episode(seasons, id)

def get_episode(seasons, id):
    for s in seasons:
        for episode in s[EPISODES_KEY]:
            if episode[IMDB_ID_KEY] == id:
                return episode
    
    raise HTTPException(status_code=HTTP_404, detail=ERROR_MSG_SEASON)

def comment_episode_imp(id, comment, series_title):
    seasons = get_database(series_title)
    comment_episode(seasons, id, comment)
    update_database(series_title, seasons)
    
def comment_episode(seasons, id, comment):
    for s in seasons:
        for episode in s[EPISODES_KEY]:
            if episode[IMDB_ID_KEY] == id:
                episode[COMMENTS_KEY].append(comment)

def get_comments_per_episode_imp(id, series_title):
    seasons = get_database(series_title)
    episode = get_episode(seasons, id)
    return episode[COMMENTS_KEY]