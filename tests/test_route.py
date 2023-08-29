import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    client = app.test_client()
    yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Guilherme Marques Lopes' in response.data

def test_projeto1_route(client):
    response = client.get('/projeto1')
    assert response.status_code == 200
    assert b'Projeto 1' in response.data
