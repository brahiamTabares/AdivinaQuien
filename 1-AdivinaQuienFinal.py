##Parcial 1 de inteliegencia artificial:Brahiam David Tabares Vallejo y Sandra Milena Quintero Leal

from tkinter import *
from tkinter import ttk
import tkinter
import random

import tk

personaje1 = {

    "name": "spiderman",
    "genero": "hombre",
    "color": "rojo y azul",
    "arma": "no tiene",
    "poder": "telaraña, sentido aracnido, escalar"
}
personaje2 = {

    "name": "batman",
    "genero": "hombre ",
    "color": "negro ",
    "arma": "shuriken, pistola de escalada, bombas de humo",
    "poder": "no tiene"
}
personaje3 = {
    "name": "superman",
    "genero": "hombre",
    "color": "Rojo y azul",
    "arma": "no tiene",
    "poder": "Volar, rayos x, visión de calor"
}
personaje4 = {

    "name": "thor",
    "genero": "hombre",
    "color": "Rojo y azul",
    "arma": "Martillo, rompetormentas, hacha",
    "poder": "volar, super fuerza"
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
    "color": "Rojo y azul",
    "arma": "escudo",
    "poder": "superfuerza y agilidad"
}
personaje7 = {

    "name": "deadpool",
    "genero": "hombre",
    "color": "Negro y rojo",
    "arma": "Pistolas, espadas",
    "poder": "Súper curación, inmortalidad, regeneración"
}
personaje8 = {

    "name": "chapulin colorado",
    "genero": "hombre",
    'color': "Rojo y amarillo",
    "arma": "chipote chillon ",
    "poder": "no tiene"
}
personaje9 = {

    "name": "mujer maravilla",
    "genero": "mujer",
    "color": "Rojo, azul y dorado",
    "arma": "Látigo, brazaletes, espada",
    "poder": "super fuerza"
}

personaje10 = {

    "name": "hulk",
    "genero": "hombre",
    "color": "Verde",
    "arma": "no tiene",
    "poder": "Mucha fuerza"
}

personaje11 = {

    "name": "iron man",
    "genero": "hombre",
    "color": "Rojo y amarillo",
    "arma": "El traje",
    "poder": "Multimillonario e inteligene"
}

personaje12 = {

    "name": "tormenta",
    "genero": "mujer",
    "color": "Gris",
    "arma": "No tiene",
    "poder": "Control del clima"
}

listaPersonajes= [personaje1,personaje2,personaje3,personaje4,personaje5,personaje7,
                  personaje6,personaje8,personaje9, personaje10, personaje11, personaje12]
personajeAleatorio = listaPersonajes[random.randint(0, 13)]


def adivinar(personaje):
    if personaje == personajeAleatorio["name"]:
        label_resultado["text"] = "¡Acertaste!"

    else:
        label_resultado["text"] = "Equivocado"

# columna , fila y expanción de la columna , adaptacion del boton en la pantalla
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

    hulk.grid(column=0, row=9, sticky=(W, N, E, S))
    ironMan.grid(column=1, row=9, sticky=(W, N, E, S))
    deadpool.grid(column=2, row=9, sticky=(W, N, E, S))
    tormenta.grid(column=3, row=9, sticky=(W, N, E, S))


root = Tk()
root.title("Adivina quien")
root.geometry("+400+120")

marcoInterfaz = ttk.Frame(root)

marcoInterfaz.grid(column=0, row=0, sticky= (W, N, E, S))

marcoInterfaz.columnconfigure(0, weight=1)
marcoInterfaz.columnconfigure(1, weight=1)
marcoInterfaz.columnconfigure(2, weight=1)
marcoInterfaz.columnconfigure(3, weight=1)
marcoInterfaz.columnconfigure(4, weight=1)

marcoInterfaz.rowconfigure(0, weight=1)
marcoInterfaz.rowconfigure(1, weight=1)
marcoInterfaz.rowconfigure(2, weight=1)
marcoInterfaz.rowconfigure(3, weight=1)
marcoInterfaz.rowconfigure(4, weight=1)
marcoInterfaz.rowconfigure(5, weight=1)
marcoInterfaz.rowconfigure(6, weight=1)
marcoInterfaz.rowconfigure(7, weight=1)
marcoInterfaz.rowconfigure(8, weight=1)
marcoInterfaz.rowconfigure(9, weight=1)
marcoInterfaz.rowconfigure(10, weight=1)

label_titulo = tkinter.Label(marcoInterfaz, text ="\nPulsa play para iniciar",
                             font="Fixedsys 20",anchor="center")
label_titulo.grid(row = 1, column = 0, columnspan=4, pady = 8)

label_caracteristica = tkinter.Label(marcoInterfaz, text ="Selecciona la pista:",
                                     font="Fixedsys 20",foreground="blue")

label_heroes = tkinter.Label(marcoInterfaz, text ="Si ya sabes quién es\n selecciona el héroe",
                             font="Fixedsys 20")

label_genero = tkinter.Label(marcoInterfaz,font="Fixedsys 15", background="black", foreground="white")
label_color = tkinter.Label(marcoInterfaz,font="Fixedsys 15", background="black", foreground="white")
label_arma = tkinter.Label(marcoInterfaz,font="Fixedsys 15", background="black", foreground="white")
label_poder = tkinter.Label(marcoInterfaz,font="Fixedsys 15", background="black", foreground="white")
label_resultado = tkinter.Label(marcoInterfaz, font="Fixedsys 20",foreground="orange",background="black")


genero = ttk.Button(marcoInterfaz, text="Genero", command = lambda: mostrarGenero())
color = ttk.Button(marcoInterfaz, text="Color", command = lambda: mostrarColor())
arma = ttk.Button(marcoInterfaz, text="Arma", command = lambda: mostrarArma())
poder = ttk.Button(marcoInterfaz, text="Poder", command = lambda: mostrarPoder())

chapulinColorado = ttk.Button(marcoInterfaz, text="Chapulin Colorado",
                              command = lambda: adivinar("chapulin colorado"))
batman = ttk.Button(marcoInterfaz, text="Batman", command = lambda: adivinar("batman"))
superman = ttk.Button(marcoInterfaz, text="Superman", command = lambda: adivinar("superman"))
mujerMaravilla = ttk.Button(marcoInterfaz, text="Mujer Maravilla",
                            command = lambda: adivinar("mujer maravilla"))
panteraNegra = ttk.Button(marcoInterfaz, text="Pantera Negra", command = lambda: adivinar("pantera negra"))
spiderman = ttk.Button(marcoInterfaz, text="Spiderman", command = lambda: adivinar("spiderman"))
thor = ttk.Button(marcoInterfaz, text="Thor", command = lambda: adivinar("thor"))
capitanAmerica = ttk.Button(marcoInterfaz, text="Capitan America",
                            command = lambda: adivinar("capitan america"))
deadpool = ttk.Button(marcoInterfaz, text="Deadpool", command = lambda: adivinar("deadpool"))
hulk = ttk.Button(marcoInterfaz, text="Hulk", command = lambda: adivinar("hulk"))
ironMan = ttk.Button(marcoInterfaz, text="Iron Man", command = lambda: adivinar("iron man"))
tormenta = ttk.Button(marcoInterfaz, text="Tormenta", command = lambda: adivinar("tormenta"),)

play = ttk.Button(marcoInterfaz, text="Play", command= lambda: iniciarJuego())
play.grid(column= 0, row=2, columnspan=4, sticky= ( W, N, E, S))

root.mainloop()

