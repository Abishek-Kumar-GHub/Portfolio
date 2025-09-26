# wsgi.py
from app import app    # imports the `app` Flask instance from app.py

if __name__ == "__main__":
    app.run()