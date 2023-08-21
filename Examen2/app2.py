from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_floreria"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index2():
    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM tbFlores')
    consulta = curSelect.fetchall()

    return render_template('index2.html', flores=consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        VNombre = request.form['txtNombre']
        VCantidad = request.form['txtCantidad']
        VPrecio = request.form['txtPrecio']

        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO tbFlores (nombre, cantidad, precio) VALUES (%s, %s, %s)', (VNombre, VCantidad, VPrecio))
        mysql.connection.commit()

    flash('La flor fue guardada correctamente :)')
    return redirect(url_for('index2'))

@app.route('/tabla')
def tabla():
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM tbFlores')
    consulta = curEditar.fetchall()
    return render_template('tablaf.html', flores=consulta)

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM tbFlores WHERE id = %s', (id,))
    consulta = curEditar.fetchone()

    # Actualizar la flor
    if request.method == 'POST':
        nuevoNombre = request.form['txtNombre']
        nuevaCantidad = request.form['txtCantidad']
        nuevoPrecio = request.form['txtPrecio']

        curActualizar = mysql.connection.cursor()
        curActualizar.execute('UPDATE tbFlores SET nombre = %s, cantidad = %s, precio = %s WHERE id = %s', (nuevoNombre, nuevaCantidad, nuevoPrecio, id))
        mysql.connection.commit()

        flash('La flor ha sido actualizada correctamente :)')
        return redirect(url_for('index2'))

    return render_template('editar2.html', flor=consulta)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        curBuscar = mysql.connection.cursor()
        curBuscar.execute('SELECT * FROM tbFlores WHERE nombre LIKE %s', (f'%{nombre}%',))
        consulta = curBuscar.fetchall()
        return render_template('buscarflor.html', flores=consulta)

    return render_template('buscarflor.html')

def eliminar(id):
    curEliminar = mysql.connection.cursor()
    curEliminar.execute('DELETE FROM tbFlores WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Flor eliminada correctamente', 'success')
    return redirect(url_for('buscar'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)



