from config.bd import db, ma, app

class Department(db.Model):
    __tablename__ = 'Department'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('Company.id'))
    name = db.Column(db.String(50))

    def __init__(self, id, company_id, name):
        self.id = id
        self.company_id = company_id
        self.name = name


with app.app_context():
    db.create_all()

class DepartmentSchema(ma.Schema):
    class Meta:
        fields = ('id','company_id', 'name')
