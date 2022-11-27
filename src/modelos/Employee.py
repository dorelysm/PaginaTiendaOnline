from config.bd import db, ma, app

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('Department.id'))
    name = db.Column(db.String(50))
    salary = db.Column(db.Integer)

    def __init__(self, id, department_id, name, salary):
        self.id = id
        self.department_id = department_id
        self.name = name
        self.salary = salary


with app.app_context():
    db.create_all()

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id','department_id', 'name', 'salary')
