from unittest import mock

from app import app
from fastapi.testclient import TestClient


client = TestClient(app.app)


class TestRequestAccess:
    def test_simple(self):
        with mock.patch('client.client.request_access', return_value=True) as api_request_access:
            response = client.post('/request_access', json={'ids': [1, 2], 'scopes': ['scope1', 'scope2']},
                                   headers={'access-token': 'accessToken123'})
        assert response.status_code == 200
        assert response.json() is True
        api_request_access.assert_called_once_with(['1#scope1', '2#scope2'], 'accessToken123')
