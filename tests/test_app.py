import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from demo import app


def test_index_route():
    client = app.test_client()
    response = client.get("/index")
    assert response.status_code == 200
