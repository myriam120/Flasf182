from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL


# Inicializacion del servidor Flask 
app= Flask(__name__)

#configuracion para la conexion a BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "db_fruteria"

app.secret_key='mysecretkey'

mysql= MySQL(app)
#Declaracion de ruta 

#ruta Index o ruta principal  http://localhost:5000
# ruta se compone de nombre y funcion 
@app.route('/')
def index1():
    curSelect = mysql.connection.cursor()
    curSelect.execute('select * from tbfrutas')
    consulta = curSelect.fetchall()
    #print(consulta)
    
    return render_template('index1.html', listAlbums = consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        VFruta = request.form['txtFruta']
        VTemporada = request.form['txtTemporada']
        VPrecio = request.form['txtPrecio']
        VStock = request.form['txtStock']
        #print(titulo, artista, anio)
        cs = mysql.connection.cursor()
        cs.execute('insert into tbfrutas (fruta, temporada, precio, stock) values(%s,%s,%s,%s)', (VFruta,VTemporada,VPrecio,VStock))    
        mysql.connection.commit()
        
    flash('La fruta fue guardada correctamente :)')
    return redirect(url_for('index1'))

@app.route('/tabla')
def tabla():
    curEditar = mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas')
    consulId = curEditar.fetchone()
    return render_template('tabla.html', album = consulId)

@app.route('/editar/<id>')
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id= %s', (id,))
    consulId = curEditar.fetchone()
    return render_template('tabla.html', album = consulId)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        VFruta = request.form['txtFruta']
        VTemporada = request.form['txtTemporada']
        VPrecio = request.form['txtPrecio']
        VStock = request.form['txtStock']
        
        curAct = mysql.connection.cursor()
        curAct.execute('update tbfrutas set fruta=%s, temporada=%s, precio=%s stock=%s where id =%s', (VFruta, VTemporada, VPrecio,VStock, id))
        mysql.connection.commit()
        
    flash('La fruta a sido actualizada :)')
    return redirect(url_for('index1'))


@app.route('/borrar/<id>')
def borrar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id= %s', (id,))
    consulId = curEditar.fetchone()
    return render_template('tabla.html', album = consulId)

@app.route('/eliminar/<id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        curEli = mysql.connection.cursor()
        curEli.execute('delete from tbfrutas where id=%s', (id,))
        mysql.connection.commit()
        flash('El álbum ha sido eliminado :)')
    return redirect(url_for('index1'))

#Ejecucion
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    