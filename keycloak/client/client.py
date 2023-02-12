import aiohttp
from client.constants import HOST, PORT, REALM


BASE_URL = f'http://{HOST}:{PORT}/realms/{REALM}/'


async def request_access(permissions: list[str], access_token: str) -> bool:
    """
    audience

    This parameter is optional. The client identifier of the resource server to which the client is seeking
    access. This parameter is mandatory in case the permission parameter is defined. It serves as a hint to
    Keycloak to indicate the context in which permissions should be evaluated.
    """
    # todo what about audience parameter???

    payload = {'permission': permissions, 'response_mode': 'decision'}
    headers = {'Authorization': f'Bearer {access_token}'}
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{BASE_URL}protocol/openid-connect/token', data=payload, headers=headers) as response:
            if response.status == 404:
                return False
            response = await response.json()
            return response['result']
