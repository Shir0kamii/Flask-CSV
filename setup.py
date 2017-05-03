import os

from setuptools import setup


def read(fname):
    fullname = os.path.join(os.path.dirname(__file__), fname)
    with open(fullname) as fp:
        content = fp.read()
    return content


setup(
    name="Flask-CSV",
    version="0.2.0",
    url="https://github.com/Shir0kamii/Flask-CSV",
    author_email="shir0kamii@gmail.com",
    description="Easily render CSVs within any flask application",
    long_description=read("README.rst"),
    download_url="https://github.com/Shir0kamii/Flask-CSV/tags",
    platforms="any",
    py_modules=["flask_csv"],
    install_requires=[
        "csvalidate",
        "Flask",
        "marshmallow"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
