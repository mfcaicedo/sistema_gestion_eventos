
from ast import Try
from flask import Blueprint, Flask, flash, jsonify, render_template, request

from flask_sqlalchemy import SQLAlchemy
from models.evento import Evento

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/dbeventos"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

eventos = Blueprint('eventos', __name__)

@app.route('/index')
def index():
    
    #consulta base de datos 
    eventos = Evento.query.all()
    
    
    return render_template('index.html', eventos=eventos)

def query_string():
    print(request)
    
@app.route("/formulario")
def formulario():
    return render_template('registrar.html')
@app.route('/insertar', methods=['POST'])
def insertar():
    try:
        datos = request.form
        #Creo objeto Evento 
        objEvento = Evento(datos['codigo'], datos['nombre'], datos['entradas'], datos['fecha'])
        #Inserto objeto de evento a la sesion, (paso valores)
        db.session.add(objEvento)
        db.session.commit() #confirmo inserción 
        # evento = objEvento.query.all() #guardo en la db 
        
        return "correcto" 
    except Exception as ex:
        return "error" 

@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html')

@app.route('/reservar')
def reservar():
    return render_template('reservar.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)