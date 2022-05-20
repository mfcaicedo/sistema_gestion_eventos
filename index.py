
from flask import Flask, jsonify, render_template, request
# from flask_mysqldb  import MySQL

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/dbeventos"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Evento(db.Model):
    eve_id = db.Column(db.Integer, primary_key=True)
    eve_codigo = db.Column(db.Integer,nullable=False)
    eve_nombre = db.Column(db.String(80), nullable=False)
    eve_entradas = db.Column(db.Integer, nullable=False)
    eve_fecha = db.Column(db.DateTime, nullable=False)
    
#Inserción en la base de datos, paso valores
db.session.add(Evento(eve_codigo=10, eve_nombre='Exposicion', eve_entradas=100, eve_fecha='23-05-22'))
db.session.commit() #confirmo inserción 
evento = Evento.query.all() #inserta en la base de datos 

@app.route('/index')
def index():
    return render_template('index.html')

def query_string():
    print(request)

@app.route('/eventos')
def eventos():
    data = {}

@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)