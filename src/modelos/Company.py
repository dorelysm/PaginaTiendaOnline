from config.bd import db, ma, app

class Company(db.Model):
    __tablename__ = 'Company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, name):
        self.id = id
        self.name = name

with app.app_context():
    db.create_all()

class CompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')