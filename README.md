# FastAPI architecture PoC

- Scheduler
- WebSocket
- DI
- Repository
- APIs

## Installation

```bash
pipx install poetry
poetry install

# Start MariaDB
docker run --detach \
    --name fastapi-arch-db \
    --env MARIADB_USER=user \
    --env MARIADB_PASSWORD=password \
    --env MARIADB_DATABASE=my_db \
    --env MARIADB_ROOT_PASSWORD=root-pw \
    --publish 23306:3306 \
    mariadb:latest

# Run server
./run.sh

# Run test
./test.sh
```

## APIs

```bash
# list of robots
curl http://localhost:8000/robots

# get one
curl http://localhost:8000/robots/1

# get non-exists robot
curl http://localhost:8000/robots/99

# Create new robot
curl -X POST -d '{"name": "Robot2"}' --header 'Content-Type: application/json' http://localhost:8000/robots

# Update robot
curl -X PUT -d '{"name": "Robot3"}' --header 'Content-Type: application/json' http://localhost:8000/robots/3

# Update non-exists robot
curl -X PUT -d '{"name": "Robot99"}' --header 'Content-Type: application/json' http://localhost:8000/robots/99

# Delete robot
curl -X DELETE http://localhost:8000/robots/1

# Delete non-exists robot
curl -X DELETE http://localhost:8000/robots/99
```
