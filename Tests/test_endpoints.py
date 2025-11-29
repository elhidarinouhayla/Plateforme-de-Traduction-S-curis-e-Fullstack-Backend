import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



from fastapi.testclient import TestClient
import pytest
from main import app


@pytest.fixture
def client():
     return TestClient(app)

def test_register(client):
     
     resp = client.post("/register")
     assert resp.status_code == 200





def test_login(client):

    resp = client.post("/login", json={"username": "user1", "password": "pass"})
    assert resp.status_code == 200



def test_translate(client):
     
     resp = client.post("/translate", json={"username": "user1", "password": "pass"})
     assert resp.status_code == 200







    
