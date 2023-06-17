from flask import Flask, render_template,request

# Inicializacion del servidor Flask 
app= Flask(__name__)

#configuracion para la conexion a BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "dbflask"

#Declaracion de ruta 

#ruta Index o ruta principal  http://localhost:5000
# ruta se compone de nombre y funcion 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        print(titulo, artista, anio)

    return "La info del Album llego a su ruta Amigo ;)"


@app.route('/eliminar')
def eliminar():
    return "Se elimino"

#Ejecucion
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    