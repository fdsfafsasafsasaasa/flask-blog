from flask_login.utils import login_required
from werkzeug.security import check_password_hash
from flask import render_template, request
from werkzeug.utils import redirect

from pakt_blog.models import db, User, Post

from pakt_blog import app

from flask_login import login_user

@app.route("/")
def home():
    return render_template("index.html", posts=db.session.query(Post).all())

@app.route("/post/<id>/")
def get_post(id):

    for post in db.session.query(Post).all():
        if post.id == int(id):
            return render_template("post.html", post=post)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        username, password = request.form.get('username'), request.form.get('password')

        user = User.query.filter_by(name=username).first()

        if not user:
            return redirect("/")

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect("/create")
        
        return redirect("/")

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "GET":
        return render_template("create.html")

    if request.method == "POST":
        db.session.add(
            Post(
                name = request.form.get("title"),
                body = request.form.get("body")
            )
        )

        db.session.commit()

        return redirect("/")