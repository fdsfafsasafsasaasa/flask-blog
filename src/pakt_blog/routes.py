import flask_login
from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, request, flash
from flask_login.utils import login_required
from werkzeug.utils import redirect

from pakt_blog.models import db, User, Post

from pakt_blog import app, login_manager

from flask_login import login_user

@app.route("/")
def home():
    return render_template("index.html", posts=db.session.query(Post).all().reverse())

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
            flash("User does not exist")
            return redirect("/register")

        correct_password = check_password_hash(user.password, password)

        if correct_password:
            login_user(user)
            return redirect("/")

        if not correct_password:
            flash("Incorrect credentials")
            return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":

        username, password = request.form.get('username'), request.form.get('password')

        if User.query.filter_by(name=username).first():
            flash("Username already taken.")
            return redirect("/register")

        user = User(name=username, password=generate_password_hash(password))

        db.session.add(user)
    
        db.session.commit()

        login_user(user)

        return redirect("/")

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "GET":
        return render_template("create.html")   

    if request.method == "POST":

        if Post.query.filter_by(name=request.form.get("title")):
            flash("Post title already taken.")
            return redirect("/create")

        post = Post(
                name = request.form.get("title"),
                body = request.form.get("body"),
                author = flask_login.current_user.name
            )

        db.session.add(
           post
        )

        db.session.commit()

        post = Post.query.filter_by(name=post.name)

        return redirect(f"/post/{post.id}")

@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/")