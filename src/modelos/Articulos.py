from config.bd import db, ma, app

class Articulos (db.Model):
    __tablename__ = "Articulo"

    id  = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(70), unique=True)
    Precio = db.Column(db.Float())
    Imagen = db.Column(db.String(100))
    Descripcion = db.Column(db.String(100))

    def __init__(self, Nombre, Precio, Imagen, Descripcion):
        self.Nombre = Nombre
        self.Precio = Precio
        self.Imagen = Imagen
        self.Descripcion = Descripcion

with app.app_context():
    db.create_all()

class ArticuloSchema (ma.Schema):
    class Meta:
        fields = ('id', 'Nombre', 'Precio', 'Imagen', 'Descripcion')
