# app.py
from flask import Flask, redirect, abort

app = Flask(__name__)


@app.route("/<path:raw_string>")
def get_raw_path(raw_string):
    if "://" not in raw_string:
        abort(400, description="Invalid URI: '://' is missing")
    return redirect(raw_string, code=307)


if __name__ == "__main__":
    app.run()
