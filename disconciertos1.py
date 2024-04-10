"""""
import tkinter as tk
from tkinter import messagebox
import json
usuarios = []
concierto = "Los inquietos del vallenato"
root = tk.Tk()
root.title("Los inquietos del vallenato") 
#REQUISITO DE  crear usuario"
class Usuario:
    def _init_(self, nombre, apellido, edad, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.tipo = tipo  # VIP o estándar
        self.reservas = []

    def _str_(self):
        return f"{self.nombre} {self.apellido} ({self.tipo}) - Edad: {self.edad}"
#Crear reserva#
    def crear_reserva(self, concierto, cantidad_boletos):
        reserva = {"concierto": concierto, "cantidad_boletos": cantidad_boletos}
        self.reservas.append(reserva)
        print(f"Reserva creada para el concierto {concierto} - {cantidad_boletos} boletos")
#Generar factura#
    def generar_factura(self):
        factura = {"usuario": str(self), "reservas": self.reservas}
        with open(f"{self.nombre}_{self.apellido}_factura.json", "w") as file:
            json.dump(factura, file)
        print("Factura generada y almacenada.")
#Crear bar#
class Bar:
    def _init_(self):
        self.bebidas = {
            "alcoholicas": [
                {"nombre": "Cerveza", "precio": 5.000},
                {"nombre": "Vino tinto", "precio": 10.000},
                {"nombre": "Ron", "precio": 80.000},
                {"nombre": "Whisky", "precio": 120.000},
                {"nombre": "Gin Tónico", "precio": 70.000}
            ],
            "no_alcoholicas": [
                {"nombre": "Agua", "precio": 1.000},
                {"nombre": "Refresco de cola", "precio": 3.000},
                {"nombre": "Jugo de naranja", "precio": 2.000},
                {"nombre": "Limonada", "precio": 2.500},
                {"nombre": "Té helado", "precio": 2.000}
            ]
        }
        self.boletos_vip_disponibles = 40
        self.palco_disponible = True
#Mostrar bebidas
    def mostrar_bebidas(self, tipo_usuario):
        print("Bebidas disponibles:")
        for categoria in self.bebidas:
            print(f"{categoria.capitalize()}:")
            for bebida in self.bebidas[categoria]:
                precio = bebida["precio"]
                if tipo_usuario == "VIP":
                    precio *= 0.75
                print(f"{bebida['nombre']} - ${precio:.2f}")

    def seleccionar_bebida(self, tipo_usuario, bebida, cantidad):
        for categoria in self.bebidas:
            for b in self.bebidas[categoria]:
                if bebida == b["nombre"]:
                    precio = b["precio"]
                    if tipo_usuario == "VIP":
                        precio *= 0.75
                    total = precio * cantidad
                    print(f"{cantidad} {bebida} seleccionada(s) - Total: ${total:.2f}")
                    return
        print(f"{bebida} no está en el menú")
"""
