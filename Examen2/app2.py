from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Inicialización del servidor Flask
app = Flask(__name__)

# Configuración para la conexión a BD
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_floreria"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index2():
    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM dbflores')
    consulta = curSelect.fetchall()

    return render_template('index2.html', flores=consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        VNombre = request.form['txtNombre']
        VCantidad = request.form['txtCantidad']
        VPrecio = request.form['txtPrecio']
        #print(titulo, artista, anio)
        cs = mysql.connection.cursor()
        cs.execute('insert into dbflores (nombre, cantidad, precio) values(%s,%s,%s)', (VNombre,VCantidad,VPrecio)); 
        mysql.connection.commit()
        
    flash('La flor fue guardada correctamente :)')
    return redirect(url_for('index2'))


@app.route('/tabla')
def tabla():
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM dbflores')
    consulta = curEditar.fetchall()
    return render_template('tablaflores.html', flores=consulta)

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM dbflores WHERE id = %s', (id,))
    consulta = curEditar.fetchone()

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        curBuscar = mysql.connection.cursor()
        curBuscar.execute('SELECT * FROM dbflores WHERE fruta LIKE %s', (f'%{nombre}%',))
        consulta = curBuscar.fetchall()
        return render_template('buscarflor.html', frutas=consulta)

    return render_template('buscarflor.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)


