# tests/test_app.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello' in response.data

def test_health_route():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200