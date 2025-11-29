import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



from fastapi.testclient import TestClient
import pytest
from main import app


@pytest.fixture
def client():
     return TestClient(app)



def test_endpoint(client):
    
#  tester endpoint register
    resp = client.post("/register", json={"username": "user", "password": "pass"})
    assert resp.status_code == 200
    
#  tester endpoint login
    resp = client.post("/login", json={"username": "user", "password": "pass"})
    assert resp.status_code == 200

    token = resp.json()["token"]
    
#  tester endpoint translate
    headers = {"Authorisation": f"bearer {token}"}
    resp = client.post("/translate", json={"text": "text", "language": "fr-en"}, headers=headers)
    assert resp.status == 200
    assert "translation" in resp.json()

     
     






    
