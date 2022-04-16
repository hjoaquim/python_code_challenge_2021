from fastapi import FastAPI
from typing import Optional
from log_config import *
from const import *
from database_builder import create_series_database_imp
from database_parser import *

app = FastAPI()


"""
To get the application up and running type the following on your terminal:
(if needed: pip install uvicorn)
uvicorn main:app --reload
"""

"""
Interactive API docs:
Go to http://127.0.0.1:8000/docs.
You will see the automatic interactive API documentation (provided by Swagger UI) (https://github.com/swagger-api/swagger-ui).
"""


@app.post("/create_series_database")
async def create_series_database(series_title: Optional[str] = SERIES_TITLE_GOT):
    create_series_database_imp(series_title)
    message = SUCESS_MSG_CREATE_SERIES_DATABASE
    logging.info(LOG_TEMPLATE.format('create_series_database', series_title, message))
    return {"message": message}

@app.get("/get_episodes_per_season")
async def get_episodes_per_season(season: int, series_title: Optional[str] = SERIES_TITLE_GOT):
    data = get_episodes_per_season_imp(season, series_title)
    message = SUCESS_MSG
    logging.info(LOG_TEMPLATE.format('get_episode_per_season', [season, series_title], message))
    return {"message": message, "data": data}

@app.get("/get_episode_details")
async def get_episode_details(id: str, series_title: Optional[str] = SERIES_TITLE_GOT):
    data = get_episode_details_imp(id, series_title)
    message = SUCESS_MSG
    logging.info(LOG_TEMPLATE.format('get_episode_details', [id, series_title], message))
    return {"message": message, "data": data}

@app.post("/comment_episode")
async def comment_episode(id: str, comment: str, series_title: Optional[str] = SERIES_TITLE_GOT):
    comment_episode_imp(id, comment, series_title)
    message = SUCESS_MSG
    logging.info(LOG_TEMPLATE.format('comment_episode', [id, comment, series_title], message))
    return {"message": message}

@app.get("/get_comments_per_episode")
async def get_comments_per_episode(id: str, series_title: Optional[str] = SERIES_TITLE_GOT):
    data = get_comments_per_episode_imp(id, series_title)
    message = SUCESS_MSG
    logging.info(LOG_TEMPLATE.format('get_comments_per_episode', [id, series_title], message))
    return {"message": message, "data": data}