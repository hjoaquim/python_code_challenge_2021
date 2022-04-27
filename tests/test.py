import sys
from fastapi import FastAPI
from fastapi.testclient import TestClient
sys.path.insert(0, DIR)
from const import *
from main import app


client = TestClient(app)


def test_create_series_database():
    response = client.post("/create_series_database")
    assert response.status_code == 200
    assert response.json() == {"message": SUCESS_MSG_CREATE_SERIES_DATABASE}
