import PySimpleGUI as sg
import json
import os
from config import CONFIGURATION_PATH

#from menu_inicio import ventana_menu

#ARCHIVOS_FIGURACE = os.path.abspath(os.path.join(__file__, '..', '..','..','..','archivos_figurace'))
archivo_configuracion=os.path.join(CONFIGURATION_PATH, 'configuracion.json')

def crear_ventana_configuracion():
    layout=[ 
            [sg.Combo(["Facil","Normal","Dificil","Experto"],size=(30,1),key="-LISTA-DIFICULTAD-",readonly=True)],
            # [sg.Input("Ingrese el tiempo limite por ronda")],
            # [sg.Input("Ingrese la cantidad de rondas por juego  ")],
            # [sg.Input("Ingrese el puntaje a sumar por cada respuesta correcta")],
            # [sg.Input("Ingrese el puntaje a restar por cada respuesta incorrecta")],
            # [sg.Input("Ingrese el nivel")],
             [sg.Button("Confirmar configuracion",key="-CONFIRMAR-CONFIGURACION-")],
             [sg.Button("Volver al menu de inicio",key="-VOLVER-MENU-INICIO-")]
    ]
    return sg.Window("",layout=layout,margins=(100,100))

def crear_archivo_configuracion():
    # configuracion=[
    #     { 
    #       "facil":{"tiempo":"60s","cant_rondas":3,"punt_sum_resp":40,"punt_res_resp":5,"cant_car_mostrar":5}
    #      ,"normal":{"tiempo":"30s","cant_rondas":5,"punt_sum_resp":30,"punt_res_resp":10,"cant_car_mostrar":4}
    #      ,"dificil":{"tiempo":"20s","cant_rondas":7,"punt_sum_resp":20,"punt_res_resp":15,"cant_car_mostrar":3}
    #      ,"experto":{"tiempo":"15s","cant_rondas":10,"punt_sum_resp":10,"punt_res_resp":20,"cant_car_mostrar":2}
    #     }
    # ]

    configuracion={ 
          "facil":{"tiempo":"60s","cant_rondas":3,"punt_sum_resp":40,"punt_res_resp":5,"cant_car_mostrar":5}
         ,"normal":{"tiempo":"30s","cant_rondas":5,"punt_sum_resp":30,"punt_res_resp":10,"cant_car_mostrar":4}
         ,"dificil":{"tiempo":"20s","cant_rondas":7,"punt_sum_resp":20,"punt_res_resp":15,"cant_car_mostrar":3}
         ,"experto":{"tiempo":"15s","cant_rondas":10,"punt_sum_resp":10,"punt_res_resp":20,"cant_car_mostrar":2}
        }
    

    try:
        with open(archivo_configuracion,"w",encoding="utf-8") as archivo_conf:
            json.dump(configuracion,archivo_conf,indent=4)
    except:
        with open(archivo_configuracion,"w",encoding="utf-8") as archivo_conf:
            json.dump(configuracion,archivo_conf,indent=4)       

def obtener_dificultad(values):
    with open(archivo_configuracion,"r",encoding="utf-8") as arch_conf:
        dicc_dificultad=json.load(arch_conf)
    if(not values["-LISTA-DIFICULTAD-"].lower() in ["facil","normal","dificil","experto"]):
                sg.Popup("Dificultad invalida,vaya a la configuracion y elija nuevamente la dificultad")
                return None,None 
    else:                   
        #return dicc_dificultad[0][values["-LISTA-DIFICULTAD-"].lower()],values["-LISTA-DIFICULTAD-"]
        return dicc_dificultad[values["-LISTA-DIFICULTAD-"].lower()],values["-LISTA-DIFICULTAD-"]


def ventana_configuracion(ventana):
    crear_archivo_configuracion()    
    vent_configuracion=crear_ventana_configuracion()   
    while True:
        event,values=vent_configuracion.read()
        if(event in(None,"-VOLVER-MENU-INICIO-")):
            vent_configuracion.close()
            ventana.un_hide()
            return None,None
        elif(event=="-CONFIRMAR-CONFIGURACION-"):
            if(values["-LISTA-DIFICULTAD-"]!=""):
                dicc_dificultad,dificultad=obtener_dificultad(values)
                vent_configuracion.close()
                ventana.un_hide()
                return dicc_dificultad,dificultad
            else:
                sg.Popup("Dificultad invalida,por favor elija una dificultad")
                #pass    
            #break
    #return dicc_dificultad,dificultad
    #ventana_configuracion.close()
    #return dicc_dificultad,dificultad                




