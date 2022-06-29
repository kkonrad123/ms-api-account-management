import main
from fastapi.testclient import TestClient

client = TestClient(main.app)

# create temporary account dictionary
main.accounts = {
    1: {"name": "joe", "balance": 500, "active": True, "description": None},
    2: {"name": "smith", "balance": 400, "active": True, "description": None},
    3: {"name": "example", "balance": 300, "active": True, "description": None}
}

def test_health_status():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": True}

def test_account_creation():
    response = client.post("/accounts/4", json={"name": "new account name", "balance": 350000})
    assert response.status_code == 201
    assert response.json() == {
        "name": "new account name",
        "balance": 350000,
        "active": True,
        "description": None
    }

def test_existent_account_creation():
    response = client.post("/accounts/4", json={"name": "yet another account", "balance": 1})
    assert response.status_code == 409
    assert response.json() == {
        "detail": "Account exists"
    }

def test_account_removal():
    response = client.delete("/accounts/4")
    assert response.status_code == 200
    assert response.json() == True

def test_nonexistent_account_removal():
    response = client.delete("/accounts/4")
    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found"}

def test_account_read():
    response = client.get("/accounts/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "joe",
        "balance": 500,
        "active": True,
        "description": None
    }

def test_nonexistent_account_read():
    response = client.get("/accounts/4")
    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found"}
