from app import db

class Book(db.Model):
    id = db.column(db.integer, primary_key=True, autoincrement=True)
    title = db.column(db.string)
    description = db.column(db.string)