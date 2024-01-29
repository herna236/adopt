from flask_sqlalchemy import SQLAlchemy


GENERIC_IMAGE = "https://fastly.picsum.photos/id/695/200/300.jpg?hmac=8XcLTGOEhNglzXNZlLLbH0z6flQivZ2F6LML0Wah8lI"

db = SQLAlchemy()



class Pet(db.Model):
    """Pet"""

    __tablename__ = "Pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    name = db.Column(db.Text, nullable=False)
    
    species = db.Column(db.Text, nullable = False)

    photo_url = db.Column(db.Text, nullable = True)
    
    age = db.Column(db.Integer, nullable = True)

    notes = db.Column(db.Text, nullable = True) 
    
    available = db.Column(db.Boolean, nullable = False, default = True)
   
    def image_url(self):
        """Return image for pet"""

        return self.photo_url or GENERIC_IMAGE

def connect_db(app):
    """Connect this database to provided Flask app.
    """

    db.app = app
    db.init_app(app)
 