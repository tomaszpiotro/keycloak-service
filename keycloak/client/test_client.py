from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from client.client import request_access


class TestClient:

    @patch('aiohttp.ClientSession')
    @pytest.mark.asyncio
    async def test_request_access_simple(self, mocked_session):
        session = MagicMock()
        session.post.return_value.__aenter__.return_value = AsyncMock(status=200)
        session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value={'result': True})
        mocked_session.return_value.__aenter__.return_value = session
        reply = await request_access(['1$scope1'], 'token1')
        assert reply is True
        session.post.assert_called_once_with(
            'http://keycloak.org:80/realms/realm/protocol/openid-connect/token',
            data={'permission': ['1$scope1'], 'response_mode': 'decision'},
            headers={'Authorization': 'Bearer token1'}
        )

    @patch('aiohttp.ClientSession')
    @pytest.mark.asyncio
    async def test_request_access_404(self, mocked_session):
        session = MagicMock()
        session.post.return_value.__aenter__.return_value = AsyncMock(status=404)
        mocked_session.return_value.__aenter__.return_value = session
        reply = await request_access(['1$scope1'], 'token1')
        assert reply is False
