from app import db


class SDK(db.Model):
    __tablename__ = "sdks"

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(), unique=True)
    ad_requests = db.Column(db.Integer, default=0)
    impressions = db.Column(db.Integer, default=0)
