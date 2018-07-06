from flask import Flask
from flask_csv import send_csv

app = Flask(__name__)


@app.route("/")
def index():
    return send_csv([{"id": 42, "foo": "bar"}, {"id": 91, "foo": "baz"}],
                    "test.csv", ["id", "foo"])


if __name__ == '__main__':
    app.run()
