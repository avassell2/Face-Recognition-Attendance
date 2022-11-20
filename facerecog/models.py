from main import db

class person(db.Model):
    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(60), unique=True, nullable=False)
        image= db.Column(db.String(20), nullable=False)
        
