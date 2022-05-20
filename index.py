
from flask import Flask, jsonify, render_template, request

from flask_mysqldb  import MySQL

app = Flask(__name__)



#Conexión a MySql
# app.config["MYSQL_USER"]="root"
# app.config["MYSQL_PASSWORD"]="root"
# app.config["MYSQL_DB"]="dbeventos"
# app.config["MYSQL_PORT"]="3307"
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "dbeventos"
app.config["MYSQL_PORT"] = "3307"

# app.config['MYSQL_CHARSET']='utf-8'
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}


conexion = MySQL(app) #establece la conexión de mi app con la db

@app.route('/index')
def index():
    return render_template('index.html')

def query_string():
    print(request)

@app.route('/eventos')
def eventos():
    data = {}
   # try:
    # print(f" que imprimer {conexion}")
    
    cursor = conexion.connection.cursor()
    # print("antes del sql")
    sql = "SELECT eve_codigo, eve_nombre, eve_entradas, eve_fecha FROM evento"
    cursor.execute(sql)
    print("antes del fetch")
    eventos = cursor.fetchall()
    print(f"que imprime {eventos}")
    data['mensaje'] = 'Exito' 
    #except Exception as ext:
     #   data['mensaje'] = 'Erorr'
    return jsonify(data)
    # return render_template('eventos.html')

@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)