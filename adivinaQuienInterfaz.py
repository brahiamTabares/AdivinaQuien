##Parcial 1 de inteliegencia artificial:Brahiam David Tabares Vallejo y Sandra Milena Quintero Leal

''' NORMATIVA
Solo puede utilizar turtle, pygame, matplotlib, numpy, random, pandas en
python
2. Juego Adivina Quien
3. Parte gráfica.
4. Explicación sobre el tipo de agente, la resolución de problemas.
5. Informe.

ITEMS PONDERACIÓN
- Elementos utilizados y parámetros contemplados para el diseño 0.8
- Selección de funciones, métodos y algoritmos 0.8
- Validación del funcionamiento final 0.8
- Seguimiento clase 0.7
- Documento – sustentación por video 0.95
- Conclusiones – sustentación por video
'''

import pygame
import sys
from pygame.locals import *
import random


 #Configuración de la ventana del juego
pygame.init()
width = 800
height = 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Adivina Quién")
avatar = pygame.image.load("batman.png")
posX, posY = (10, 40)
while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


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

    "name": "thor ",
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

"name": "chespirito",
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
gameChosenCharacter= listaPersonajes[random.randint(0,8)]
#print(gameChosenCharacter)

def print_all_chars(list_of_chars):

    for personaje in  list_of_chars:
        charName=''
        printList = []

        for item in personaje:
            if item == "name":
                charName=personaje[item]
            else:
                printList.append(personaje[item])

        print(charName)
        print(printList)


bienvenido=("Bienvenido al juego Adivina Quién"
            "Adivina el personaje ")
print(("Respuestas Aceptadas:(list),(genero),(color),(armna),(poder), or (adivina nombre)"))


#print_all_chars(listaPersonajes)
for personaje in listaPersonajes:
    print(personaje["name"])
userCommand= ''
gameStatus= ''
userQuestionCout = 0

while userCommand !='quit' and gameStatus != 'over':

    #userCommand=input("What would you like to do?  (genero/color/arma/poder)")

    if userQuestionCout < 2:
        userCommand = input("What would you like to do?  (genero/color/arma/poder)")
        if userCommand == "genero":
            print(gameChosenCharacter["genero"])
            userQuestionCout += 1
        elif userCommand == "color":
            print(gameChosenCharacter["color"])
            userQuestionCout += 1

        elif userCommand == "arma":
            print(gameChosenCharacter["arma"])
            userQuestionCout += 1

        elif userCommand == "poder":
            print(gameChosenCharacter["poder"])
            userQuestionCout += 1

        elif userCommand == "list":
            print_all_chars(listaPersonajes)

        elif userCommand =='guess':

            userGuess = input("you ve run out of questions,with character would you like to guess? ")

            if userGuess ==gameChosenCharacter['name']:
                gameStatus = "over"
                print("you chose correctly!")

            else:
                gameStatus = 'over'
                print("you did not choose correctly")

        else:
             print("youd did no enter a valid command, please tray again")

    else:
        userGuess = input("you ve run out of questions,with character would you like to guess? ")

        if userGuess ==gameChosenCharacter['name']:

            gameStatus = 'over'
            print("you chose correctly")

        else:

            gameStatus = 'over'
            print("you did not choose correctly")
