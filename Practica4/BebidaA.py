import sqlite3
import tkinter as tk
from tkinter import messagebox

class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio
        
class AlmaBedidas:
    def __init__(self):
        self.connection = sqlite3.connect("C:/Users/majo0/Documents/GitHub/Flas182/Practica4/AlmacenBebidas.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("create table is not exists bebidad (id interger primary key, nombre text, clasificacion text, marca text, precio real )")
        self.connection.commit()
        
def __del__(self):
    self.connection.close()
    
def agregaB(self, bebida):
    self.cursor.execute("INSERT INTO bebidas VALUES (?, ?, ?, ?, ?)", (bebida.id, bebida.nombre, bebida.clasificacion, bebida.marca, bebida.precio))
    self.connection.commit()
    
def eliminarB(self, id):
    self.cursor.execute("DELETE FROM bebidas WHERE id = ?", (id,))
    self.connection.commit()
        
def actualizarB(self, id, nombre, clasificacion, marca, precio):
    self.cursor.execute("UPDATE bebidas SET nombre = ?, clasificacion = ?, marca = ?, precio = ? WHERE id = ?", (nombre, clasificacion, marca, precio, id))
    self.connection.commit()
        
def mostrarB(self):
    self.cursor.execute("SELECT * FROM bebidas")
    rows = self.cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Nombre: {row[1]}, Clasificación: {row[2]}, Marca: {row[3]}, Precio: {row[4]}")

def calcularPP(self):
    self.cursor.execute("SELECT AVG(precio) FROM bebidas")
    promedio = self.cursor.fetchone()[0]
    return promedio

def contarBM(self, marca):
    

    