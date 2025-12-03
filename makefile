install:
	poetry install

run:
	uvicorn src.outsera_challenge.main:app

run-dev:
	uvicorn src.outsera_challenge.main:app --reload

revision:
	alembic revision --autogenerate -m "create table movie"

migrate:
	alembic upgrade head

test:
	pytest tests