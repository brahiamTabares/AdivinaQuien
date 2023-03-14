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
import random

print("Prueba")
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

listaPersonajes = [personaje1,personaje2,personaje3,personaje4,personaje5,personaje7,personaje6,personaje8,personaje9]
personajeSeleccionado = listaPersonajes[random.randint(0,8)]
print(personajeSeleccionado)

def PersonajerCaracteristica(listaCaracteristicas):

     for personaje in  listaCaracteristicas:
         personajeNombre=""
         printList=[]

         for item in personaje:
             if item == "name":
                 personajeNombre==personaje[item]
             else:
                 printList.append(personaje[item])
                 print(personajeNombre)
                 print(printList)

PersonajerCaracteristica(listaPersonajes)
print(("Bienvenido a adivina quien , tienes un nombre random de un personaje, y adivina quien es "))
print(("Respuestas Aceptadas:(list),(genero),(color),(armna),(poder), or (adivina nombre)"))

usuarioComando= ""
gameStatus=""
userQuestionCout = 0

while usuarioComando !='quit' and gameStatus !='over':

    usuarioComando= input("Cual caracteristica te gusta? (list/genero/color/arma/poder)")

    if userQuestionCout < 2:
        if usuarioComando == "genero":
            print(personajeSeleccionado["genero"])
            userQuestionCout +=1

        elif usuarioComando == "color":
            print(personajeSeleccionado["color"])
            userQuestionCout += 1

        elif usuarioComando == "arma":
            print(personajeSeleccionado["arma"])
            userQuestionCout += 1

        elif usuarioComando == "arma":
            print(personajeSeleccionado["arma"])
            userQuestionCout += 1

        elif usuarioComando == "list":
            PersonajerCaracteristica(listaPersonajes)

        elif usuarioComando == "respuesta" :
            respuestaUsuario = input("te has quedado sin conjeturas,cual personaje te gustaria adivinar?")

            if respuestaUsuario == personajeSeleccionado["name"]:
                gameStatus = "over"
                print("tu respuesta es correcta" )
            else:
                gameStatus = "over"
                print("tu respuesta no es correcta")
        else:
            respuestaUsuario = input("te has quedado sin conjeturas,cual personaje te gustaria adivinar?")

            if respuestaUsuario == personajeSeleccionado["name"]:
                gameStatus = "over"
                print("tu respuesta  es correcta! ")
            else:
                gameStatus = "over"
                print("tu respuesta no es correcta. ")

