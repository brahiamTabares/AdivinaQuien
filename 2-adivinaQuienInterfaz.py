##Parcial 1 de inteliegencia artificial:Brahiam David Tabares Vallejo y Sandra Milena Quintero Leal

from tkinter import *
from tkinter import ttk
import tkinter
import random

personaje1 = {

    "name": "spiderman",
    "genero": "hombre",
    "color": ["rojo", "azul", "rojo y azul", "azul y rojo"],
    "arma": "no tiene",
    "poder": ["telaraña", "sentido aracnido", "escalar"]
}
personaje2 = {

    "name": "batman",
    "genero": "hombre ",
    "color": "negro ",
    "arma": ["shuriken", "pistola de escalada", "bombas de humo"],
    "poder": "no tiene"
}
personaje3 = {
    "name": "superman",
    "genero": "hombre",
    "color": ["rojo", "azul", "rojo y azul", "azul y rojo"],
    "arma": "no tiene",
    "poder": ["volar", "rayos laser", "rayos x"]
}
personaje4 = {

    "name": "thor",
    "genero": "hombre",
    "color": ["rojo", "azul", "rojo y azul", "azul y rojo"],
    "arma": ["martillo", "rompetormentas", "hacha"],
    "poder": ["volar", "super fuerza"]
}
personaje5 = {

"name": "pantera negra",
"genero": "hombre",
"color": "negro",
"arma": "traje",
"poder": "no tiene"
}
personaje6 = {

"name": "capitan america",
"genero": "hombre",
"color": ["rojo", "azul", "rojo y azul", "azul y rojo"],
"arma": "escudo",
"poder": ["superfuerza", "agilidad"]
}
personaje7 = {

"name": "deadpool",
"genero": "hombre",
"color": ["rojo", "negro", "negro y rojo", "rojo y negro"],
"arma": ["pistolas", "espadas"],
"poder": ["super curacion", "inmortalidad", "regeneracion"]
}
personaje8 = {

"name": "chapulin colorado",
"genero": "hombre",
'color': ["rojo y amarillo", "rojo", "amarillo y rojo"],
"arma": "chipote chillon ",
"poder": "no tiene"
}
personaje9 = {

"name": "mujer maravilla",
"genero": "mujer",
"color": ["dorado", "rojo,azul y dorado", "azul y rojo", "rojo y azul"],
"arma": ["latigo", "brazaletes", "espada"],
"poder": ["super fuerza"]
}

listaPersonajes= [personaje1,personaje2,personaje3,personaje4,personaje5,personaje7,personaje6,personaje8,personaje9]
personajeAleatorio = listaPersonajes[random.randint(0, 8)]


def adivinar(personaje):
    if personaje == personajeAleatorio["name"]:
        label_resultado["text"] = "¡Acertaste!"

    else:
        label_resultado["text"] = "Equivocado como la carrera que elegí"


    label_resultado.grid(column=0, row=10, columnspan=4,  sticky=(W, N, E, S))


def mostrarGenero():
    label_genero.grid(column=0, row=5, sticky=(W, N, E, S))
    label_genero["text"] = personajeAleatorio["genero"]

def mostrarColor():
    label_color.grid(column=1, row=5, sticky=(W, N, E, S))
    label_color["text"] = personajeAleatorio["color"]

def mostrarArma():
    label_arma.grid(column=2, row=5, sticky=(W, N, E, S))
    label_arma["text"] = personajeAleatorio["arma"]

def mostrarPoder():
    label_poder.grid(column=3, row=5, sticky=(W, N, E, S))
    label_poder["text"] = personajeAleatorio["poder"]

def iniciarJuego():
    personajeAleatorio = listaPersonajes[random.randint(0, 8)]
    label_caracteristica.grid(row=3, column=0, columnspan=4, pady=8)

    genero.grid(column=0, row=4, sticky=(W, N, E, S))
    color.grid(column=1, row=4, sticky=(W, N, E, S))
    arma.grid(column=2, row=4, sticky=(W, N, E, S))
    poder.grid(column=3, row=4, sticky=(W, N, E, S))

    label_heroes.grid(row=6, column=0, columnspan=4, pady=8)

    chapulinColorado.grid(column=0, row=7, sticky=(W, N, E, S))
    batman.grid(column=1, row=7, sticky=(W, N, E, S))
    superman.grid(column=2, row=7, sticky=(W, N, E, S))
    mujerMaravilla.grid(column=3, row=7, sticky=(W, N, E, S))

    panteraNegra.grid(column=0, row=8, sticky=(W, N, E, S))
    spiderman.grid(column=1, row=8, sticky=(W, N, E, S))
    thor.grid(column=2, row=8, sticky=(W, N, E, S))
    capitanAmerica.grid(column=3, row=8, sticky=(W, N, E, S))

    deadpool.grid(column=2, row=9, sticky=(W, N, E, S))


windowRoot = Tk()
windowRoot.title("Adivina quien")
windowRoot.geometry("+500+80")

mainFrame = ttk.Frame(windowRoot)

mainFrame.grid(column=0, row=0, sticky= ( W, N, E, S) )

mainFrame.columnconfigure(0,weight=1)
mainFrame.columnconfigure(1,weight=1)
mainFrame.columnconfigure(2,weight=1)
mainFrame.columnconfigure(3,weight=1)
mainFrame.columnconfigure(4,weight=1)

mainFrame.rowconfigure(0,weight=1)
mainFrame.rowconfigure(1,weight=1)
mainFrame.rowconfigure(2,weight=1)
mainFrame.rowconfigure(3,weight=1)
mainFrame.rowconfigure(4,weight=1)
mainFrame.rowconfigure(5,weight=1)
mainFrame.rowconfigure(6,weight=1)
mainFrame.rowconfigure(7,weight=1)
mainFrame.rowconfigure(8,weight=1)
mainFrame.rowconfigure(9,weight=1)
mainFrame.rowconfigure(10,weight=1)

label_titulo = tkinter.Label(mainFrame, text = "Pulsa play para iniciar", font="arial 20")
label_titulo.grid(row = 1, column = 0, columnspan=4, pady = 8)

label_caracteristica = tkinter.Label(mainFrame, text = "Selecciona la pista:", font="arial 20")

label_heroes = tkinter.Label(mainFrame, text = "Si ya sabes quien es, selecciona el heroe", font="arial 20")

label_genero = tkinter.Label(mainFrame)
label_color = tkinter.Label(mainFrame)
label_arma = tkinter.Label(mainFrame)
label_poder = tkinter.Label(mainFrame)
label_resultado = tkinter.Label(mainFrame, font="arial 20")


genero = ttk.Button(mainFrame, text="Genero", command = lambda: mostrarGenero())
color = ttk.Button(mainFrame, text="Color", command = lambda: mostrarColor())
arma = ttk.Button(mainFrame, text="Arma", command = lambda: mostrarArma())
poder = ttk.Button(mainFrame, text="Poder", command = lambda: mostrarPoder())

chapulinColorado = ttk.Button(mainFrame, text="Chapulin Colorado", command = lambda: adivinar("chapulin colorado"))
batman = ttk.Button(mainFrame, text="Batman", command = lambda: adivinar("batman"))
superman = ttk.Button(mainFrame, text="Superman", command = lambda: adivinar("superman"))
mujerMaravilla = ttk.Button(mainFrame, text="Mujer Maravilla", command = lambda: adivinar("mujer maravilla"))
panteraNegra = ttk.Button(mainFrame, text="Pantera Negra", command = lambda: adivinar("pantera negra"))
spiderman = ttk.Button(mainFrame, text="Spiderman", command = lambda: adivinar("spiderman"))
thor = ttk.Button(mainFrame, text="Thor", command = lambda: adivinar("thor"))
capitanAmerica = ttk.Button(mainFrame, text="Capitan America", command = lambda: adivinar("capitan america"))
deadpool = ttk.Button(mainFrame, text="Deadpool", command = lambda: adivinar("deadpool"))


play = ttk.Button(mainFrame, text="Play", command= lambda: iniciarJuego())
play.grid(column= 0, row=2, columnspan=4, sticky= ( W, N, E, S))


windowRoot.mainloop()