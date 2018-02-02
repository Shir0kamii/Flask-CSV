#########
Flask-CSV
#########

Easily render CSVs within any flask application

Install
#######

Flask-CSV is packaged and you can use pip to install it::

    pip install flask_csv


How to use ?
############

Flask-CSV has a simple hepler method named `send_csv` which allows you to send
csv files in flask endpoints. It takes an iterable of `dict`, a filename and a
list of fields. The keys of all `dict` in the iterable must correspond to
given fields.

It will return a `Response` object with filename set and body containing the
CSV data.

You will better understand with a short example.

.. code-block:: python

    @app.route("/")
    def index():
        return send_csv([{"id": 42, "foo": "bar"}, {"id": 91, "foo": "baz"}],
                        "test.csv", ["id", "foo"])

Hitting this endpoint will return::

    id,foo
    42,bar
    91,baz


Passing additionnal parameters to `send_file`
#############################################

The remaining arguments of `send_csv` will be passed to `send_file`. For
example, to disable caching, do the following:

.. code-block:: python

    send_csv([{"id": 42, "foo": "bar"}, {"id": 91, "foo": "baz"}],
             "test.csv", ["id", "foo"], cache_timeout=0)


Change delimiter
################

You can also change the delimiter with the `delimiter` option.

.. code-block:: python

    send_csv([{"id": 42, "foo": "bar"}, {"id": 91, "foo": "baz"}],
             "test.csv", ["id", "foo"], delimiter=';')

Will result in::

    id;foo
    42;bar
    91;baz

Specifying file encoding
########################

You can also specify the encoding used to send the file, with the `encoding` option (`utf-8` by default).

.. code-block:: python

    send_csv([{"id": 42, "foo": "bar"}, {"id": 91, "foo": "baz"}],
             "test.csv", ["id", "foo"], encoding='iso-8859-1')

Use Marshmallow Schemas
#######################

You can use `Schema` from marshmallow by passing it as `schema` to `send_csv`.
If you want to keep only ids and ensure they are integers, you could do:

.. code-block:: python

    class IdSchema(Schema):
        id = fields.Integer()

    send_csv([{"id": 42, "foo": "bar"}, {"id": 91, "foo": "baz"}],
             "test.csv", ["id", "foo"], schema=IdSchema())

And that would result in this::

    id
    42
    91
