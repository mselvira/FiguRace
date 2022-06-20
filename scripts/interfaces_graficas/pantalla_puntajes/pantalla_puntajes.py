import json
import PySimpleGUI as sg
import os
from config import PUNTAJES_PATH

def crear_ventana_puntajes():
    layout=[ 
             [sg.Table(values=[[]],headings=["Nombre","Puntaje","Puntaje promedio"],key="-TABLA-FACIL-",display_row_numbers=True)],
             [sg.Table(values=[[]],headings=["Nombre","Puntaje","Puntaje promedio"],key="-TABLA-NORMAL-",display_row_numbers=True)],
             [sg.Table(values=[[]],headings=["Nombre","Puntaje","Puntaje promedio"],key="-TABLA-DIFICIL-",display_row_numbers=True)], 
             [sg.Button("Volver al menu de inicio",key="-VOLVER-MENU-INICIO-")]
    ]
    return sg.Window("",layout=layout,margins=(100,100)) 

# def traer_json_configuracion():
#     nombres=[]
#     puntajes=[]
#     promedios=[]
#     archivo_configuracion=os.path.join(PUNTAJES_PATH,'puntajes.json')
#     with open(archivo_configuracion) as arch_conf:
#         datos_configuracion=json.load(arch_conf)
#     for clave in datos_configuracion.keys():    
#         for clave,valor in datos_configuracion[clave].items():
#             nombres.append(clave)
#             puntajes.append(valor["puntaje"])
#             promedios.append(valor["puntaje"]/valor["rondas_jugadas"])
#     print(nombres)
#     print(puntajes)
#     print(promedios)

def traer_json_configuracion():
    nombres=[]
    puntajes=[]
    promedios=[]
    archivo_configuracion=os.path.join(PUNTAJES_PATH,'puntajes.json')
    with open(archivo_configuracion) as arch_conf:
        datos_configuracion=json.load(arch_conf)
    dicc={}    
    for clave_dificultad in datos_configuracion.keys():
        nombres=[]
        puntajes=[]
        promedios=[]    
        for clave_nombre,valor in datos_configuracion[clave_dificultad].items():
            nombres.append(clave_nombre)
            puntajes.append(valor["puntaje"])
            promedios.append(valor["puntaje"]/valor["rondas_jugadas"])
            dicc[clave_dificultad]={"Nombres":nombres,"puntajes":puntajes,"promedios":promedios}    
    print(dicc)
    return dicc
    
    


def ventana_puntajes():
    
    vent_puntajes=crear_ventana_puntajes()
    dicc=traer_json_configuracion()
    event,values=vent_puntajes.read()
    lista_final=[]
    for clave,valor in dicc.items():
        listas=zip(valor["Nombres"],valor["puntajes"],valor["promedios"])
        for nombre,puntaje,promedio in listas:
            print(nombre,puntaje,promedio)
            lista=[nombre,puntaje,promedio]
            print(lista)
            lista_final.append(lista)
        print(clave,":",lista_final)     
        vent_puntajes["-TABLA-"+clave.upper()+"-"].Update(values=lista_final)
        lista_final=[]
    while True:
        if(event in(None,"-VOLVER-MENU-INICIO-")):
            break
    vent_puntajes.close()
