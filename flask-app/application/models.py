from application import db


class Characters(db.Model):
    __tablename__ = 'Characters'
    char_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    race = db.Column(db.String(20), nullable=False)
    archetype = db.Column(db.String(50), nullable=False)