from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Inicialización del servidor Flask
app = Flask(__name__)

# Configuración para la conexión a BD
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_fruteria"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

# Ruta Index o ruta principal http://localhost:5000
# La ruta se compone de nombre y función
@app.route('/')
def index1():
    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM tbfrutas')
    consulta = curSelect.fetchall()

    return render_template('index1.html', listAlbums=consulta)


@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        VFruta = request.form['txtFruta']
        VTemporada = request.form['txtTemporada']
        VPrecio = request.form['txtPrecio']
        VStock = request.form['txtStock']

        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO tbfrutas (fruta, temporada, precio, stock) VALUES (%s, %s, %s, %s)', (VFruta, VTemporada, VPrecio, VStock))
        mysql.connection.commit()

    flash('La fruta fue guardada correctamente :)')
    return redirect(url_for('index1'))


@app.route('/tabla')
def tabla():
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM tbfrutas')
    consulta = curEditar.fetchall()
    return render_template('tabla.html', frutas=consulta)


@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM tbfrutas WHERE id = %s', (id,))
    consulta = curEditar.fetchone()

    if request.method == 'POST':
        VFruta = request.form['txtFruta']
        VTemporada = request.form['txtTemporada']
        VPrecio = request.form['txtPrecio']
        VStock = request.form['txtStock']

        curAct = mysql.connection.cursor()
        curAct.execute('UPDATE tbfrutas SET fruta = %s, temporada = %s, precio = %s, stock = %s WHERE id = %s', (VFruta, VTemporada, VPrecio, VStock, id))
        mysql.connection.commit()

        flash('La fruta ha sido actualizada :)')
        return redirect(url_for('index1'))

    return render_template('editar.html', fruta=consulta)


@app.route('/eliminar/<id>', methods=['GET', 'POST'])
def eliminar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM tbfrutas WHERE id = %s', (id,))
    consulta = curEditar.fetchone()

    if request.method == 'POST':
        curEli = mysql.connection.cursor()
        curEli.execute('DELETE FROM tbfrutas WHERE id = %s', (id,))
        mysql.connection.commit()
        flash('La fruta ha sido eliminada :)')
        return redirect(url_for('index1'))

    return render_template('eliminar.html', fruta=consulta)


@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        curBuscar = mysql.connection.cursor()
        curBuscar.execute('SELECT * FROM tbfrutas WHERE fruta LIKE %s', (f'%{nombre}%',))
        consulta = curBuscar.fetchall()
        return render_template('buscar.html', frutas=consulta)

    return render_template('buscar.html')


# Ejecución
if __name__ == '__main__':
    app.run(port=5000, debug=True)

    