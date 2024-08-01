from manage import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.String(100), nullable=False)
  