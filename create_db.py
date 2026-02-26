from api import db, app, VideoModel

with app.app_context():
    db.create_all()
    print("Database created successfully.")
