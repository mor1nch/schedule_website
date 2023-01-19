# api
@app.route("/api/post/")
@app.route("/api/post")
def api_posts():
    posts = load_posts()
    return jsonify(posts)


@app.route("/api/post/<int:pk>/")
@app.route("/api/post/<int:pk>")
def api_post(pk):
    post = load_posts(pk)
    return jsonify(post)

# в app
if __name__ == '__main__':
    app.run()
# tests_api в отдельную папку tests
from pytest import fixture

@fixture
def client():
    client = app.test_client()


def test_api_posts(client):
    resp = client.get("/api/post/")
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    assert len(resp.json) > 0
def test_api_post(client):
    resp = client.get("/api/post/1")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert len(resp.json) > 0