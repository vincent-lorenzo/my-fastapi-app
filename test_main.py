from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    # Instead of checking for JSON, we check if "<html>" is in the text
    assert "<html>" in response.text
    assert "Prime Checker Pro" in response.text

def test_prime_checker():
    # This part stays the same because the "Logic" didn't change!
    response_prime = client.get("/check-prime/7")
    assert response_prime.json() == {"number": 7, "is_prime": True}

    response_not_prime = client.get("/check-prime/10")
    assert response_not_prime.json() == {"number": 10, "is_prime": False}