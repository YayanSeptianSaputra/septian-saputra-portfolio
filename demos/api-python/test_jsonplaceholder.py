"""API test Python (pytest + requests) pada API demo publik JSONPlaceholder. Tanpa data privat."""
import pytest
import requests

BASE = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def get(path):
    return requests.get(f"{BASE}{path}", timeout=TIMEOUT)


def test_get_post_status_body_dan_schema():
    r = get("/posts/1")
    assert r.status_code == 200
    body = r.json()
    assert set(body) == {"userId", "id", "title", "body"}
    assert body["id"] == 1
    assert isinstance(body["title"], str) and body["title"]


def test_daftar_posts_berisi_100_data_dengan_id_unik():
    posts = get("/posts").json()
    assert len(posts) == 100
    assert len({p["id"] for p in posts}) == 100


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_filter_posts_per_user_hanya_milik_user_itu(user_id):
    posts = get(f"/posts?userId={user_id}").json()
    assert posts and all(p["userId"] == user_id for p in posts)


@pytest.mark.parametrize("path", ["/posts/0", "/posts/101", "/posts/999999"])
def test_boundary_id_di_luar_rentang_mengembalikan_404(path):
    # boundary value: id valid 1..100
    assert get(path).status_code == 404


def test_buat_post_mengembalikan_201_dan_id_baru():
    payload = {"title": "uji", "body": "isi", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code == 201
    created = r.json()
    assert created["title"] == "uji" and created["id"] == 101


def test_hapus_post_mengembalikan_200():
    assert requests.delete(f"{BASE}/posts/1", timeout=TIMEOUT).status_code == 200


def test_response_time_wajar():
    assert get("/posts/1").elapsed.total_seconds() < 2
