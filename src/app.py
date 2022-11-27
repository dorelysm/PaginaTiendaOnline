from flask import Flask, redirect, request, jsonify, json, session, render_template

from config.bd import app, db
from modelos.Articulos import Articulos, ArticuloSchema
from modelos.User import User, UsersSchema

#extra
from modelos.Company import Company, CompanySchema
from modelos.Department import Department, DepartmentSchema
from modelos.Employee import Employee, EmployeeSchema


articulo_schema = ArticuloSchema()
articulos_schema = ArticuloSchema(many=True)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)


@app.route('/', methods=['GET'])
def index():
    
    return render_template("login.html")

@app.route('/ingresar', methods=['POST'])
def ingresar():
    email = request.form['email']
    password = request.form['password']
    user = db.session.query(User.id).filter(User.email == email, User.password == password).all()
    resultado = users_schema.dump(user)

    if len(resultado)>0:
        session['usuario'] = email
        return redirect('/larticulos')
    else:
        return redirect('/')

@app.route('/larticulos', methods=['GET'])
def larticulos():
    if 'usuario' in session:
        all_articulos = Articulos.query.all()
        result_articulos = articulos_schema.dump(all_articulos)
        return render_template("larticulos.html",articulos = result_articulos, usuario= session['usuario'])
    else:
        return redirect('/')
   

@app.route('/cerrar')
def cerrar():
    session.pop('usuario',None)
    return redirect('/')

@app.route('/guardar', methods=['POST'] )
def guardar_articulo():
    Nombre = request.form['Nombre']
    Precio = request.form['Precio']
    Imagen = request.form['Imagen']
    Descripcion = request.form['Descripcion']
    new_articulo = Articulos(Nombre, Precio, Imagen, Descripcion)
    db.session.add(new_articulo)
    db.session.commit()
    return redirect('/larticulos')

@app.route('/eliminar', methods=['GET'] )
def eliminar():
    id = request.args.get('id')
    articulos = Articulos.query.get(id)
    db.session.delete(articulos)
    db.session.commit()
    return articulo_schema.dump(articulos)

@app.route('/articulos', methods=['GET'] )
def articulos():
    id = request.args.get('id')
    articulos = Articulos.query.get(id)
    restul_articulo = articulo_schema.dump(articulos)
    return jsonify(restul_articulo)

@app.route('/actualizar', methods=['POST'] )
def actualizar():
    id = request.form['id']
    Nombre = request.form['Nombre']
    Precio = request.form['Precio']
    articulo = Articulos.query.get(id)
    articulo.Nombre = Nombre
    articulo.Precio = Precio
    db.session.commit()
    return redirect('/larticulos')

@app.route('/consultar3tabla', methods=['GET'])
def consultar3tablas():
    datos= {}
    resultado = db.session.query(Employee,Department, Company). \
        select_from(Employee).join(Department).join(Company).all()
    i=0
    for employee,department,company  in resultado:
        i+=1
        datos={
            i:{
                'Ename': employee.name,
                'Dname': department.name,
                'Cname': company.name
            }
        }
    print(datos)
    return "Algo"

if __name__ == "__main__":
    app.run(debug=True, port=4000)