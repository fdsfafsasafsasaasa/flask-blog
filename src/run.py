from flask_sqlalchemy import _DebugQueryTuple
from pakt_blog import app, db

if __name__ == "__main__":
    db.create_all()

    app.run()