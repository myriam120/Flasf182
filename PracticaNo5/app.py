from flask import Flask

# Inicializacion del servidor Flask 
app= Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""
app.config['MYSQL_DB']= "dbflask"

#Declaracion de ruta 

#ruta Index o ruta principal  http://localhost:5000
# ruta se compone de nombre y funcion 
@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/guardar')
def guardar():
    return "Se guardo el album en la BD"

@app.route('/eliminar')
def eliminar():
    return "Se elimino"

#Ejecucion
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    