import pytest
from app import app

# Setup test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test 1 — Check home page works
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    print("✅ Home page is working!")

# Test 2 — Check health page works
def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    print("✅ Health page is working!")

# Test 3 — Check health returns healthy status
def test_health_status(client):
    response = client.get('/health')
    data = response.get_json()
    assert data['status'] == 'healthy'
    print("✅ Health status is healthy!")