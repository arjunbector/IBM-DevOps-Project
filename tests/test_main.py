import pytest
import json

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == 'Flask DevOps Pipeline'

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_get_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'users' in data
    assert len(data['users']) == 2

def test_create_user(client):
    user_data = {
        'name': 'Test User',
        'email': 'test@example.com'
    }
    response = client.post('/api/users', 
                          data=json.dumps(user_data),
                          content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['user']['name'] == 'Test User'

def test_create_user_invalid_data(client):
    response = client.post('/api/users', 
                          data=json.dumps({}),
                          content_type='application/json')
    assert response.status_code == 400