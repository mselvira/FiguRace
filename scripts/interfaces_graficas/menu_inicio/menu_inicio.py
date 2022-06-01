import sys,os


sys.path.append('/home/ubuntu/Escritorio/Python2022/Python_TP/scripts/interfaces_graficas/pantalla_juego')
sys.path.append('/home/ubuntu/Escritorio/Python2022/Python_TP/scripts/interfaces_graficas/perfil')
sys.path.append('/home/ubuntu/Escritorio/Python2022/Python_TP/scripts/interfaces_graficas/pantalla_configuracion')
sys.path.append('/home/ubuntu/Escritorio/Python2022/Python_TP/scripts/interfaces_graficas/pantalla_puntajes')

# INTERFACES_GRAFICAS = os.path.abspath(os.path.join(__file__, '..', '..','..','..','scripts','interfaces_graficas'))
# perfil=os.path.join(INTERFACES_GRAFICAS, 'perfil')
# pantalla_juego=os.path.join(INTERFACES_GRAFICAS, 'pantalla_juego')
# pantalla_configuracion=os.path.join(INTERFACES_GRAFICAS, 'pantalla_configuracion')
# pantalla_puntajes=os.path.join(INTERFACES_GRAFICAS, 'pantalla_puntajes')

import PySimpleGUI as sg    
import json 
import os
from perfil import ventana_perfil
from pantalla_juego import ventana_juego
from pantalla_configuracion import ventana_configuracion
from pantalla_puntajes import ventana_puntajes

#Preguntar lo de los combo-box...
#Ejemplo que hizo el profe...
#DIR_FILES = os.path.abspath(os.path.join(__file__, '..', '..','..','..','data_sets'))
#print(os.path.join(DIR_FILES, 'prueba.csv'))

ARCHIVOS_FIGURACE = os.path.abspath(os.path.join(__file__, '..', '..','..','..','archivos_figurace'))
archivo_perfiles=os.path.join(ARCHIVOS_FIGURACE, 'perfiles.json')

def crear_ventana_menu():    
    sg.theme("Reddit")
    frame=[
            [sg.Text("Menu",justification="center",expand_x=True)],
            [sg.Button("Jugar",key="-BOTON-JUGAR-",size=(30,1))],
            [sg.Button("Configuracion",key="-BOTON-CONFIGURACION-",size=(30,1))],
            [sg.Button("Puntajes",key="-BOTON-PUNTAJES-",size=(30,1))],
            [sg.Button("Perfil",key="-BOTON-PERFIL-",size=(30,1))],
            [sg.Button("Salir del menu",key="-SALIR-DEL-MENU-",size=(30,1))]
    ] 
    #boton_menu_def=["Muy dificil","Dificil","Normal","Facil"]            
    col1=[
          [sg.Frame("",frame)]
    ]
    col2=[
          [sg.Text("Elija su perfil:")],
          [sg.Combo([],readonly=True,size=(30,1),key="-LISTA-NOMBRES-")]
          #[sg.Combo(["Facil","Normal","Dificil","Experto"],size=(30,1),key="-LISTA-DIFICULTAD-",default_value="Dificultad")],
          #[sg.ButtonMenu("Dificultad",menu_def=boton_menu_def,size=(30,1),key="-MENU-DIFICULTAD-")]
          #[sg.OptionMenu(values=["Muy dificil","Dificil","Normal","Facil"],default_value="Facil" ,size=(30,1),key="-MENU-DIFICULTAD-")]
    ]
    layout=[
            [sg.Text("FiguRace",justification="center",expand_x=True)],
            [sg.Column(col1,justification="center",expand_x=True,vertical_alignment="center"),sg.Column(col2,expand_y=True)]
    ]
    return sg.Window("Menu de inicio",layout=layout,margins=(100,100),finalize=True)

def cargar_nombres():
    #esto no funciona correctamente,no carga los perfiles adecuadamente
    try:
        with open(archivo_perfiles,"r") as archivo:
            lista_dic=json.load(archivo)
    except IOError:
        sg.Popup("No hay perfiles cargados,por favor cree un perfil para comenzar el juego...")        
    else:
        nombres=[dic["Nombre"] for dic in lista_dic]
        #print(nombres) 
        return nombres 

# def ventana_menu():      
#     ventana_menu,ventana_conf=crear_ventana_menu(),None
#     boton_configuracion=False
#     dificultad_por_defecto="Facil"
#     dicc_dificultad_defecto={
#         "tiempo": "60s",
#         "cant_rondas": 3,
#         "punt_sum_resp": 40,
#         "punt_res_resp": 5,
#         "car_mostrar": 5
#     }
#     while True:
#         #aca cargo los nombres
#         lista_nombres=cargar_nombres() 
#         ventana_menu["-LISTA-NOMBRES-"].Update(values=lista_nombres)
#         event,values=ventana_menu.read()   
#         if(event in (None,"-SALIR-DEL-MENU-")):
#             break
#         elif(event=="-BOTON-CONFIGURACION-"):
#             boton_configuracion=True
#             dicc_dificultad,dificultad=ventana_configuracion()
#             print(f'Dificultad:{dificultad},valores:{dicc_dificultad}')
#         elif(event=="-BOTON-JUGAR-"):  
#             if(values["-LISTA-NOMBRES-"]==""):
#                 sg.Popup("Seleccione un perfil para jugar")
#             elif(dificultad):
#                 print(dificultad,dicc_dificultad)
#                 boton_configuracion=False    
#                 ventana_juego(values["-LISTA-NOMBRES-"],dificultad,dicc_dificultad)      
#             elif(not boton_configuracion or not dificultad):
#                 sg.Popup("Vaya a configuracion para elegir una dificultad")
#         elif(event=="-BOTON-PUNTAJES-"):
#             print("Boton de puntaje")
#         elif(event=="-BOTON-PERFIL-"):  
#             ventana_perfil()
#     ventana_menu.close()




def ventana_menu():      
    ventana_menu,ventana_conf=crear_ventana_menu(),None
    dificultad_por_defecto="Facil"
    dicc_dificultad_defecto={
        "tiempo": "60s",
        "cant_rondas": 3,
        "punt_sum_resp": 40,
        "punt_res_resp": 5,
        "cant_car_mostrar": 5
    }
    boton_configuracion=False
    while True:
        #aca cargo los nombres   
        lista_nombres=cargar_nombres() 
        ventana_menu["-LISTA-NOMBRES-"].Update(values=lista_nombres)
        event,values=ventana_menu.read()   
        if(event in (None,"-SALIR-DEL-MENU-")):
            break
        elif(event=="-BOTON-CONFIGURACION-"):
            boton_configuracion=True
            ventana_menu.hide()
            dicc_dificultad,dificultad=ventana_configuracion(ventana_menu)
            print(f'Dificultad:{dificultad},valores:{dicc_dificultad}')
        elif(event=="-BOTON-JUGAR-"):  
            if(values["-LISTA-NOMBRES-"]==""):
                sg.Popup("Seleccione un perfil para jugar")    
            elif(boton_configuracion):
                if(not dificultad):
                    sg.Popup("Va a jugar con la configuracion por defecto porque no eligio una configuracion")
                    ventana_juego(values["-LISTA-NOMBRES-"],dificultad_por_defecto,dicc_dificultad_defecto,dicc_dificultad_defecto["cant_car_mostrar"])
                else:
                    ventana_juego(values["-LISTA-NOMBRES-"],dificultad,dicc_dificultad,dicc_dificultad["cant_car_mostrar"])
                    boton_configuracion=False        
            else:
                sg.Popup("Va a jugar con la configuracion por defecto porque no eligio una configuracion")
                ventana_juego(values["-LISTA-NOMBRES-"],dificultad_por_defecto,dicc_dificultad_defecto,dicc_dificultad_defecto["cant_car_mostrar"])    
        elif(event=="-BOTON-PUNTAJES-"):
            print("Boton de puntaje")
        elif(event=="-BOTON-PERFIL-"):  
            ventana_perfil()
    ventana_menu.close()

    
            

    




