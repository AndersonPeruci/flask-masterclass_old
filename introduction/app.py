from flask import Flask, request, Response, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index() -> str:
    return "<a href='/posts'>Posts<a/>"

@app.route("/posts")
@app.route("/posts/<int:post_id>")
def posts(post_id: int = False) -> str:
    data = dict(
        path = request.path,
        referrer = request.referrer,
        content_type = request.content_type,
        method = request.method,
        title = request.args.get("title"),
        post_id = post_id if post_id else False
    )
    return data

@app.route("/response")
def responses():
    return render_template("response.html")

@app.route("/redirect")
def red() -> str:
    return redirect(url_for("response"))


if __name__ == "__main__":
    app.run(debug=True)
