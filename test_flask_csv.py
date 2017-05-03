from flask import Flask
import pytest

from flask_csv import send_csv


@pytest.fixture
def client():
    app = Flask("test")

    @app.route("/")
    def index():
        return send_csv([{"id": 42, "foo": "bar"}, {"id": 91, "foo": "baz"}],
                        "test.csv", ["id", "foo"])
    return app.test_client()


def test_send_csv_filename(client):
    response = client.get("/")
    disposition = response.headers["Content-Disposition"]
    assert "test.csv" in disposition


def test_send_csv_content(client):
    response = client.get("/")
    data = response.data
    expected = b"""id,foo
42,bar
91,baz
""".replace(b'\n', b"\r\n")
    assert data == expected
