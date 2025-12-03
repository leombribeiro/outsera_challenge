import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_winners(client: AsyncClient):
    response = await client.get("/winners")
    assert response.status_code == 200

    data = response.json()

    assert "min" in data
    assert "max" in data
    assert len(data["min"]) == 2
    assert len(data["max"]) == 2
