from tkinter import ttk
from tkinter import *

import sqlite3

class AppSerie:

	def __init__(self, ventana):
		self.ventana_principal = ventana
		self.ventana_principal.title("App Series View")

		#Contenedor
		frame = LabelFrame(self.ventana_principal, text="Agregar Serie Nueva")
		frame.grid(row=0, column=0, columnspan=3, pady=20)

		#Para cargar nombres
		Label(frame, text = "Nombre serie: ").grid(row = 1, column = 0)
		self.nombre_serie = Entry(frame)
		self.nombre_serie.grid(row = 1, column = 1)

		#Para cargar temporada
		Label(frame, text = "Temporadas vistas: ").grid(row = 2, column = 0)
		self.temporada = Entry(frame)
		self.temporada.grid(row = 2, column = 1)

		#Boton de confirmacion
		ttk.Button(frame, text = "Confirmar", command = self.agregarSerie).grid(row = 3, columnspan = 2, sticky = W + E)

		#Tabla de muestra
		self.tabla = ttk.Treeview(height = 6, columns = 2)
		self.tabla.grid(row = 4, column = 0, columnspan = 2)
		self.tabla.heading('#0', text = "Serie", anchor = CENTER)
		self.tabla.heading('#1', text = "Temporadas vistas", anchor = CENTER)

		#Boton borrar
		ttk.Button(text = "BORRAR", command = self.eliminarSerie).grid(row = 5, column = 0, sticky = W + E)
		ttk.Button(text = "EDITAR", command = self.editarSerie).grid(row = 5, column = 1, sticky = W + E)

		self.mostrarSeries()

	def run_query(self, query, parametros = ()):
		miConexion=sqlite3.connect("SeriesVistas.db")
		miCursor=miConexion.cursor()
		resultado=miCursor.execute(query, parametros)
		miConexion.commit()
		return resultado

	def mostrarSeries(self):
		#vaciar tabla donde se muestran las series
		tabla_muestra = self.tabla.get_children()
		for elemento in tabla_muestra:
			self.tabla.delete(elemento)
		#relacion con BBDD	
		query = 'SELECT * FROM serie'
		resultado = self.run_query(query)
		for serie in resultado:
			self.tabla.insert('',0, text=serie[1], value=serie[2])

	def agregarSerie(self):
		query = 'INSERT INTO serie VALUES(NULL, ?, ?)'
		parametros = (self.nombre_serie.get(), self.temporada.get())
		self.run_query(query,parametros)
		self.mostrarSeries()

	def eliminarSerie(self):
		elemento_eliminar = self.tabla.item(self.tabla.selection())['values']
		query = 'DELETE FROM serie WHERE temporadas = ?'
		self.run_query(query, elemento_eliminar)
		self.mostrarSeries()

	def editarSerie(self):
		elemento_editar = self.tabla.item(self.tabla.selection())
		nombre_actual = elemento_editar['text']
		temp_actual = elemento_editar['values'][0]
		self.ventana_editar = Toplevel()
		#Nombre nuevo
		Label(self.ventana_editar, text = "Nombre actual: " + nombre_actual).grid(row = 0, column = 0)
		Label(self.ventana_editar, text = "Nombre nuevo: ").grid(row = 1, column = 0)
		nombre_nuevo = Entry(self.ventana_editar)
		nombre_nuevo.grid(row = 1, column = 1)
		#Temporada nueva
		Label(self.ventana_editar, text = "Temporada actual: " + str(temp_actual)).grid(row = 2, column = 0)
		Label(self.ventana_editar, text = "Temporada nueva: ").grid(row = 3, column = 0)
		temporada_nueva = Entry(self.ventana_editar)
		temporada_nueva.grid(row = 3, column = 1)

		Button(self.ventana_editar, text = "CONFIRMAR").grid(row = 6, column = 0)


ventana = Tk()
app = AppSerie(ventana)
ventana.mainloop()
	    
