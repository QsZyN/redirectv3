# app.py
from flask import Flask, redirect, abort, request
import re

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    url = re.sub(r":/(?!/)", r"://", request.full_path[1:])
    if "://" not in url:
        abort(400, description=f"Invalid URI: '://' is missing {url}")
    return redirect(url, code=307)


if __name__ == "__main__":
    app.run()
