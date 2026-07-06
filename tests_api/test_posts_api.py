import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
def test_get_post_por_id():
    """Valida que se pueda obtener un post existente por ID."""
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body["id"] == 1
    assert "title" in body
    assert "body" in body
    assert "userId" in body
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)
    assert isinstance(body["userId"], int)


@pytest.mark.api
def test_post_crear_post():
    """Valida la creación simulada de un post."""
    payload = {
        "title": "Automation Testing",
        "body": "Prueba automatizada con requests y pytest",
        "userId": 1,
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=10,
    )

    assert response.status_code == 201

    body = response.json()

    assert isinstance(body, dict)
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


@pytest.mark.api
def test_delete_post():
    """Valida la eliminación simulada de un post."""
    response = requests.delete(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert body == {}