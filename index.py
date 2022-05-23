
from ast import Try
from flask import Blueprint, Flask, flash, jsonify, render_template, request, redirect ,url_for, flash
from datetime import date, timedelta


from flask_sqlalchemy import SQLAlchemy
from models.evento import Evento

#coneccion a mysql
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@127.0.0.1/dbeventos"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#iniciamos la sesion para enviar mensajes
app.secret_key ='myclavesecreta'

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
        #return "correcto"
        flash('evento creado satisfactoriamente')        
        return redirect(url_for('index'))  
    except Exception as ex:
        return "error"

@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    try:
        datos = request.form
        #tomamos el valor del campo a buscar
        nombreEvento = datos['nombreEven']

        print('este es el nombre del evento\n')
        print(nombreEvento)

        #EventoResult =  Evento.query.filter_by(eve_nombre='ttt').first()
        EventoResult =  Evento.query.filter_by(eve_nombre=nombreEvento).first()

        if EventoResult:
            #print('este es el evnto \n')
            #print("codigo: " + str(EventoResult.eve_codigo) + " nombre: " + EventoResult.eve_nombre + " numero entradas: " + str(EventoResult.eve_entradas) + " fecha:" + str(EventoResult.eve_fecha))
            respuesta = "codigo: " + str(EventoResult.eve_codigo) + " nombre: " + EventoResult.eve_nombre + " numero entradas: " + str(EventoResult.eve_entradas) + " fecha:" + str(EventoResult.eve_fecha)
            flash(respuesta)
        else:
            #print('no se encontro evento')
            respuesta = 'No se encontro evento'
            flash(respuesta)
            #return respuesta

        #flash('evento econtrado satisfactoriamente')
        return redirect(url_for('busqueda'))  
    except Exception as ex:
        #return "error"
        return ex

@app.route('/reservar')
def reservar():
    return render_template('reservar.html')

@app.route('/comprar', methods=['POST'])
def comprar():
    try:
        datos = request.form
        # tomamos el valor del campo a buscar
        codigoEvento = datos['codigo_evento']
        numEntradas = datos['num_entradas']
        fecha = '21/05/2022'

        # verificamos que el codigo del evento exista
        EventoResult = Evento.query.filter_by(eve_codigo=int(codigoEvento)).first()
        
        
        print('este es el evento\n')
        print(EventoResult)

        if EventoResult:
            # si existe el evento desconamos los puestos
            EventoResult.eve_entradas = (EventoResult.eve_entradas - int(numEntradas))
            print('estas son las entradas\n')
            print(EventoResult.eve_entradas)
            #antes de modificar miramos si la fecha de compra es menor al del evento
            today = date.today()
            fechaevento = EventoResult.eve_fecha - timedelta(days=1)

            print('fecha es menor a la compra')
            if today < fechaevento:
                db.session.merge(EventoResult)
                db.session.commit() #confirmo inserción 
                flash('Reserva exitosa')
            else:
                flash('No se permite reservar voletas en esta fecha')
                return redirect(url_for('reservar'))
        else:
            # mandamos el mensaje que no existe el evento con ese codigo
            flash('No exsite evento con el codigo ingresado')

        #flash('evento econtrado satisfactoriamente')
        return redirect(url_for('reservar'))

    except Exception as ex:
        # return "error"
        return ex
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)