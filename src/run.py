import pakt_blog

if __name__ == "__main__":
    pakt_blog.db.create_all()

    pakt_blog.app.run()