from tkinter import *
from tkinter import ttk
import math

"""--------------------------Cambiar tema de la calculadora-----------------------------------"""
def temaOscuro(*args):
    estilos.configure("mainframe.TFrame", background = "#010924")

    estilos_label1.configure("Label1.TLabel",  background = "#010924", foreground="white")
    estilos_label2.configure("Label2.TLabel", background="#010924", foreground="white")

    estilos_botones_numeros.configure("Botones_numeros.TButton", background="#00044A", foreground="white")
    estilos_botones_numeros.map("Botones_numeros.TButton", background=[("active", "#020A90")])

    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#010924", foreground="white")
    estilos_botones_borrar.map("Botones_borrar.TButton", background=[("active", "#000AB1")])

    estilos_botones_operacion.configure("Botones_operacion.TButton", background="#010924", foreground="white")
    estilos_botones_operacion.map("Botones_operacion.TButton", background=[("active", "#000AB1")])
def temaClaro(*args):
    estilos.configure("mainframe.TFrame", background="#DBDBDB", foreground="black")

    estilos_label1.configure("Label1.TLabel", background="#DBDBDB", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#DBDBDB", foreground="black")

    estilos_botones_numeros.configure("Botones_numeros.TButton", background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map("Botones_numeros.TButton", background=[("active", "#B9B9B9")])

    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#CECECE", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton", background=[("active", "#858585")])

    estilos_botones_operacion.configure("Botones_operacion.TButton", background="#CECECE", foreground="black")
    estilos_botones_operacion.map("Botones_operacion.TButton", background=[("active", "#858585")])

"""--------------------------Funciones para el uso de cada boton ----------------------------"""
def ingresarValores(tecla):
    if tecla >= 'g' and tecla <= 'p':
        entrada2.set(entrada2.get() + tecla)

    if tecla == 'genero' or tecla == 'color' or tecla == 'arma' or tecla == 'poder':
        if tecla == 'genero':
            entrada1.set(entrada2.get() + 'genero')
        if tecla == 'color':
            entrada1.set(entrada2.get() + 'color')
        if tecla == 'arma':
            entrada1.set(entrada2.get() + 'poder')

        entrada2.set("")

    if tecla == "=":

        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def ingresarValoresTeclado(event):
    tecla = event.char
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)

    if tecla == 'genero' or tecla == 'color' or tecla == 'arma' or tecla == 'poder':
        if tecla == 'genero':
            entrada1.set(entrada2.get() + 'genero')
        if tecla == 'color':
            entrada1.set(entrada2.get() + 'color')
        if tecla == 'arma':
            entrada1.set(entrada2.get() + 'arma')
        if tecla == 'poder':
            entrada1.set(entrada2.get() + 'poder')



        entrada2.set("")

    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def calcularRaizCuadrada():
    entrada1.set("")
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)
def calcularLogaritmo():
    entrada1.set("")
    resultado = math.log10(float(entrada2.get()))
    entrada2.set(resultado)

def borrar(event = ""):
    inicio = 0
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])

def borrarTodo(event = ""):
    entrada2.set("")
    entrada1.set("")

"""----------------------------------------ROOT------------------------------------------"""
#Dimensionar la ventana principal
windowRoot = Tk()
windowRoot.title("Calculadora")
windowRoot.geometry("+500+80")

#Adapta el tamaño de la columna y
# fila de la ventana principal junto con los widgets
windowRoot.columnconfigure(0, weight= 1)
windowRoot.rowconfigure(0, weight= 1)

"""----------------------------------------FRAME------------------------------------------"""
#Agrega estilos a la calculadora
#Viene una por defecto llamada vista
#pero presenta problemas al agregar estilos
estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background ="#DBDBDB")

#Con la etiqueta style hará que plasme los diseños que se colocaron anteriormente
#Para que el frame esté dentro de la ventana principal
mainFrame = ttk.Frame(windowRoot, style="mainframe.TFrame")

#Adaptar los widgets a la ventana principal
mainFrame.grid(column=0, row=0, sticky= ( W, N, E, S) )

#Adaptar las columnas
mainFrame.columnconfigure(0,weight=1)
mainFrame.columnconfigure(1,weight=1)
mainFrame.columnconfigure(2,weight=1)
mainFrame.columnconfigure(3,weight=1)

#Adaptar las filas
mainFrame.rowconfigure(0,weight=1)
mainFrame.rowconfigure(1,weight=1)
mainFrame.rowconfigure(2,weight=1)
mainFrame.rowconfigure(3,weight=1)
mainFrame.rowconfigure(4,weight=1)
mainFrame.rowconfigure(5,weight=1)
mainFrame.rowconfigure(6,weight=1)
mainFrame.rowconfigure(7,weight=1)

"""----------------------------------------LABEL------------------------------------------"""
#Estilo de los labels
estilos_label1 = ttk.Style()
estilos_label1.configure("Label1.TLabel", font ="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure("Label2.TLabel", font ="arial 40", anchor="e")

#Esta creando una variable que estará vinculada a un widget
#Lo que se escriba en entrada 1 se vera reflejado en el textvariable
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainFrame, textvariable= entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row = 0, columnspan=4, sticky= ( W, N, E, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainFrame, textvariable= entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row = 1, columnspan=4, sticky= ( W, N, E, S))

"""----------------------------------------Button------------------------------------------"""
#Estilos para los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("Botones_numeros.TButton", font="arial 22", width=5,
                                  background="#FFFFFF", relief="flat")
estilos_botones_numeros.map("Botones_numeros.TButton",
                            background=[("active","#B9B9B9")])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure("Botones_borrar.TButton", font="arial 22", width= 5,
                                 background="#CECECE", relief="flat")
estilos_botones_borrar.map("Botones_borrar.TButton",
                           foreground= [("active", "#FF0000")],
                           background=[("active","#858585")])

estilos_botones_operacion = ttk.Style()
estilos_botones_operacion.configure("Botones_operacion.TButton", font="arial 22",
                                    width= 5, background="#CECECE", relief="flat")
estilos_botones_operacion.map("Botones_operacion.TButton", background=[("active","#858585")])

#Botones para los numeros 0-9
button0 = ttk.Button(mainFrame, text="genero", style="Botones_numeros.TButton", command = lambda: ingresarValores('g'))
button1 = ttk.Button(mainFrame, text="color", style="Botones_numeros.TButton", command = lambda: ingresarValores('c'))
button2 = ttk.Button(mainFrame, text="arma", style="Botones_numeros.TButton", command = lambda: ingresarValores('a'))
button3 = ttk.Button(mainFrame, text="poder", style="Botones_numeros.TButton", command = lambda: ingresarValores('p'))


#Ubicar botones en la pantalla frame
button0.grid(column=1, row=7, sticky= ( W, N, E, S))
button1.grid(column=0, row=6, sticky= ( W, N, E, S))
button2.grid(column=1, row=6, sticky= ( W, N, E, S))
button3.grid(column=2, row=6, sticky= ( W, N, E, S))



#Para realizar separaciones entre cada widget se utilizara un for
for child in mainFrame.winfo_children():
    child.grid_configure(ipady= 10, padx= 1, pady= 1)

"""-----------------------Comandos para la utilización del teclado---------------------------"""
windowRoot.bind("<KeyPress-o>",temaOscuro)
windowRoot.bind("<KeyPress-c>",temaClaro)
windowRoot.bind("<Key>", ingresarValoresTeclado)
windowRoot.bind("<KeyPress-d>", borrar)
windowRoot.bind("<KeyPress-q>", borrarTodo)

#Mostrar la ventana principal hasta que se cierre
windowRoot.mainloop()