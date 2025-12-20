from demo import app


def test_index_route():
    client = app.test_client()
    response = client.get("/index")
    assert response.status_code == 200


    # ya kho lazm tpushiha l github
    