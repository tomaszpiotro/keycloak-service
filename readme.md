keycloak auth service
====

authorization service available over REST with an asynchronous python client library to allow calling it from within a python client.

-----------

### Running

```bash
docker-compose up
```

### Running tests

```bash
docker-compose run web pytest
```

### Notes:
- I didn't study too much of keycloak docs - this implementation can be even wrong. It would be nice to have some sandbox or deeper knowledge about how it should work together
- I assumed that the point of this task is to check my async code - not necessarily my knowledge of keycloak
