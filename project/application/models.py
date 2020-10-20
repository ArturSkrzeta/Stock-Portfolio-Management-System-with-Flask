from application import db # as if from __init__ import db

class Stock(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    company = db.Column(db.String)
    open = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    commission = db.Column(db.Float)
    signal = db.Column(db.String)
    close = db.Column(db.String)
    roi = db.Column(db.Float)
    comments = db.Column(db.String)

    # s = Stock(company="Apple",open="19/10/2020",price=12.99,quantity=10,commission=0.015,signal="AT",close="",roi=0.0,comments="Long-term investment")
