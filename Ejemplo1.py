from tkinter import *

# Define la lista de personajes
personajes = [
    {"nombre": "Ana", "ojos": "marrones", "pelo": "negro", "gafas": False},
    {"nombre": "Benjamin", "ojos": "azules", "pelo": "rubio", "gafas": False},
    {"nombre": "Carla", "ojos": "verdes", "pelo": "castaño", "gafas": True},
    {"nombre": "David", "ojos": "marrones", "pelo": "pelirrojo", "gafas": True},
    {"nombre": "Elena", "ojos": "azules", "pelo": "rubio", "gafas": True},
    {"nombre": "Federico", "ojos": "verdes", "pelo": "negro", "gafas": False},
    {"nombre": "Greta", "ojos": "marrones", "pelo": "castaño", "gafas": True},
    {"nombre": "Hector", "ojos": "azules", "pelo": "pelirrojo", "gafas": False},
    {"nombre": "Ines", "ojos": "verdes", "pelo": "rubio", "gafas": False},
    {"nombre": "Juan", "ojos": "marrones", "pelo": "negro", "gafas": True}
]

# Define la función para verificar si el personaje adivinado es correcto
def verificar_personaje(nombre, seleccion):
    for personaje in personajes:
        if personaje["nombre"] == nombre:
            for atributo, valor in personaje.items():
                if atributo != "nombre":
                    if seleccion[atributo].get() != valor:
                        return False
            return True
    return False

# Crea la ventana principal
root = Tk()
root.title("Adivina Quién")

# Crea los widgets para seleccionar los atributos del personaje
frame_atributos = Frame(root)
frame_atributos.pack(side=LEFT)

seleccion = {}

Label(frame_atributos, text="Color de ojos:").grid(row=0, column=0)
opcion_ojos = StringVar(frame_atributos)
opcion_ojos.set("cualquiera")
seleccion["ojos"] = opcion_ojos
Menu(frame_atributos, optionmenu=opcion_ojos, values=["cualquiera", "marrones", "azules", "verdes"]).grid(row=0, column=1)

Label(frame_atributos, text="Color de pelo:").grid(row=1, column=0)
opcion_pelo = StringVar(frame_atributos)
opcion_pelo.set("cualquiera")
seleccion["pelo"] = opcion_pelo
Menu(frame_atributos, optionmenu=opcion_pelo, values=["cualquiera", "negro", "rubio", "castaño", "pelirrojo"]).grid(row=1, column=1)

Label(frame_atributos, text="Usa gafas:").grid(row=2, column=0)
opcion_gafas = StringVar(frame_atributos)
opcion_gafas.set("cualquiera")
seleccion["gafas"] = opcion_gaf