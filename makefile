run:
	uvicorn src.outsera_challenge.main:app --reload

revision:
	alembic revision --autogenerate -m "create table movie"

migrate:
	alembic upgrade head
