# Outsera Challenge

API developed to manage information about Golden Raspberry Awards.

## Requirements

- Python 3.14+
- Poetry

## Installation

1. Clone the repository

2. Install dependencies:
```bash
make install
```

3. Run database migrations:
```bash
make migrate
```

## Running the application

To start the development server:

```bash
make run
```

The application will be available at `http://localhost:8000`

## Endpoints

### GET /winners

Returns the list of award-winning.

**Request example:**
```bash
curl http://localhost:8000/winners
```

## Available commands

- `make install` - Install project dependencies
- `make run` - Start the development server
- `make migrate` - Run database migrations
- `make revision` - Create a new migration revision
- `make test` - Run tests

## Tests

To run tests:

```bash
make test
```

## Technologies used

- FastAPI
- Uvicorn
- SQLite
- Alembic
- Poetry
- Pytest