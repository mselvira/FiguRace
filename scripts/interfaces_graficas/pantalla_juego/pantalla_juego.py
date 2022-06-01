import json
from random import random,sample,randint
import PySimpleGUI as sg
import os,csv

#from menu_inicio import ARCHIVOS_FIGURACE

DATA_SETS = os.path.abspath(os.path.join(__file__,'..','..','..','..','data_sets_procesados'))
ARCHIVOS_FIGURACE = os.path.abspath(os.path.join(__file__,'..','..','..','..','archivos_figurace'))
#archivo_lagos=os.path.join(DATA_SETS,'lagos_argentina_procesado.csv')

def crear_ventana_juego():    
    sg.theme("Reddit")

    frame1=[
            [sg.Text("Nombre de usuario",key="-NOMBRE-USUARIO-")],
            [sg.Text("1-"),sg.Text("Algo")],
            [sg.Text("2-"),sg.Text("Algo")], 
            [sg.Text("3-"),sg.Text("Algo")],
            [sg.Text("4-"),sg.Text("Algo")],
            [sg.Text("5-"),sg.Text("Algo")],
            [sg.Text("6-"),sg.Text("Algo")],
            [sg.Text("7-"),sg.Text("Algo")],
            [sg.Text("8-"),sg.Text("Algo")],
            [sg.Text("9-"),sg.Text("Algo")],
            [sg.Text("10-"),sg.Text("Algo")],
    ] 

    frame2=[
            [sg.Text("",key="-ETIQ-CAR-0-"),sg.Text("",key="-CAR-0-")],
            [sg.Text("",key="-ETIQ-CAR-1-"),sg.Text("",key="-CAR-1-")],
            [sg.Text("",key="-ETIQ-CAR-2-"),sg.Text("",key="-CAR-2-")],
            [sg.Text("",key="-ETIQ-CAR-3-"),sg.Text("",key="-CAR-3-")],
            [sg.Text("",key="-ETIQ-CAR-4-"),sg.Text("",key="-CAR-4-")],
            [sg.Text("",key="-ETIQ-CAR-ADIVINAR-")],
            [sg.Button("Opcion1",key="-BOTON-1-")],
            [sg.Button("Opcion2",key="-BOTON-2-")],
            [sg.Button("Opcion3",key="-BOTON-3-")],
            [sg.Button("Opcion4",key="-BOTON-4-")],
            [sg.Button("Opcion5",key="-BOTON-5-")],
            [sg.Button("OK",key="-BOTON-OK-"),sg.Button("Pasar",key="-BOTON-PASAR-")]
    ]          

    col1=[
          [sg.Text("Nombre data set",key="-DATA-SET-")],
          [sg.Text("Aca va una imagen",key="-IMAGEN-")],
          [sg.Image(source=None)],
          [sg.Frame("",frame1)],
          [sg.Button("Abandonar juego",key="-BOTON-ABANDONAR-JUEGO-")]
    ]

    col2=[
          [sg.Text("Dificultad:"),sg.Text("Aca va la dificultad",key="-DIFICULTAD-")],
          [sg.Text("Tiempo:"),sg.Text("Aca va el tiempo",key="-TIEMPO-")],
          [sg.Frame("",frame2)],
    ]
    
    layout=[
            [sg.Column(col1),sg.Column(col2)]
    ]

    return sg.Window("FiguRace",layout=layout,margins=(100,100),finalize=True)

def traer_data_set(dataset):
    archivo_data_set=os.path.join(DATA_SETS,dataset)
    with open(archivo_data_set) as data_set:
        reader=csv.reader(data_set,delimiter=",") 
        header=list(next(reader))
        datos=list(reader)
    return header,datos
     

def cargar_caracteristicas_data_set(ventana,cant_car_a_mostrar):

    #traigo el dataset 
    encabezado,datos=traer_data_set('spotify_procesado.csv')
    #elijo un indice al azar para elegir un elemento al azar del dataset
    indice_dato_aleatorio=randint(0,len(datos)-1)
    dato_aleatorio=datos[indice_dato_aleatorio]
    print(dato_aleatorio)
    
    #renderizo los nombres de las caracteristicas con su respectiva caracteristica
    for i in range(cant_car_a_mostrar):
        ventana['-ETIQ-CAR-'+str(i)+'-'].Update(encabezado[i]+':')
        ventana['-CAR-'+str(i)+'-'].Update(dato_aleatorio[i])

    ventana["-ETIQ-CAR-ADIVINAR-"].Update(encabezado[-1]+':')    
    
    #renderizo los botones 
    # elijo un boton al azar(del 1 al 5) y seteo la caracteristica que corresponde 
    numero_boton_opcion_correcta=randint(1,5)
    print('indice boton opcion correcta',numero_boton_opcion_correcta)
    ventana['-BOTON-'+str(numero_boton_opcion_correcta)+'-'].Update(dato_aleatorio[-1])
    botones_restantes=[numero for numero in range(1,6) if numero != numero_boton_opcion_correcta]
    print(botones_restantes)
    #completo los botones restantes con opciones al azar
    # aca no pude hacer el import => indices_aleatorios=random.sample(range(0,len(datos)),4)
    indices_aleatorios=[randint(0,len(datos)) for i in range(4)]
    print(indices_aleatorios)

    for boton,indice in zip(botones_restantes,indices_aleatorios):
        print(datos[indice])  
        #ventana['-BOTON-'+str(boton)+'-'].Update(datos[indice][len(dato_aleatorio)-1])
        ventana['-BOTON-'+str(boton)+'-'].Update(datos[indice][-1])     	         
     

def ventana_juego(nombre,dificultad,dicc_dificultad,car_a_mostrar):    
    
    ventana_juego=crear_ventana_juego()
    ventana_juego["-NOMBRE-USUARIO-"].Update(nombre)
    ventana_juego["-DIFICULTAD-"].Update(dificultad)
    ventana_juego["-TIEMPO-"].Update(dicc_dificultad["tiempo"])

    cargar_caracteristicas_data_set(ventana_juego,car_a_mostrar)

    while True:
        event,values=ventana_juego.read()
        if(event in (None,"-BOTON-ABANDONAR-JUEGO-")):
            break
    ventana_juego.close()           

