from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    ad_requests = db.Column(db.Integer, default=0)
    impressions = db.Column(db.Integer, default=0)

