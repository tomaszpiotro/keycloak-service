import os

from client import client
from fastapi import FastAPI, Header, Request


debug = os.environ.get('DEBUG', False,)

app = FastAPI(debug=debug)


@app.post('/request_access')
async def request_access(request: Request, ids: list[int], scopes: list[str], access_token: str = Header()) -> bool:
    # TODO we could validate that len(ids) == len(scopes)
    permissions = [f'{id}#{scope}' for id, scope in zip(ids, scopes)]
    return await client.request_access(permissions, access_token)
