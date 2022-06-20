from functools import reduce
import json
from random import random, sample,randint
import PySimpleGUI as sg
import os,csv
from time import time
from uuid import uuid4
from abandonar_juego_excepcion import AbandonarJuegoExcepcion
from config import DATA_SETS_PATH, IMAGES_PATH,ESTADISTICAS_PATH,PUNTAJES_PATH


#from menu_inicio import ARCHIVOS_FIGURACE

lista_opciones_datasets=["lagos_argentina_procesado.csv","spotify_procesado.csv"]
   
# DATA_SETS = os.path.join(RESOURCES_PATH,'data_sets_procesados')
# ARCHIVOS_FIGURACE = os.path.join(CONFIGURATION_PATH,'archivos_figurace')
# #archivo_lagos=os.path.join(DATA_SETS,'lagos_argentina_procesado.csv')
# FILE_IMAGE=os.path.join(IMAGES_PATH,'imagenes')


def crear_ventana_juego(cant_car_mostrar):    
    sg.theme("Reddit")

    lista=list(map(lambda x:[sg.Text(str(x)+"-"),sg.Text("Algo",key=f"-RESPUESTA-{x}")],range(1,cant_car_mostrar+1)))
    
    # frame1=[
    #         [sg.Text("Nombre de usuario",key="-NOMBRE-USUARIO-")],
    #         [sg.Text("1-"),sg.Text("Algo")],
    #         [sg.Text("2-"),sg.Text("Algo")], 
    #         [sg.Text("3-"),sg.Text("Algo")],
    #         [sg.Text("4-"),sg.Text("Algo")],
    #         [sg.Text("5-"),sg.Text("Algo")],
    #         [sg.Text("6-"),sg.Text("Algo")],
    #         [sg.Text("7-"),sg.Text("Algo")],
    #         [sg.Text("8-"),sg.Text("Algo")],
    #         [sg.Text("9-"),sg.Text("Algo")],
    #         [sg.Text("10-"),sg.Text("Algo")],
    # ]
     
    frame1=[[sg.Text("Nombre de usuario",key="-NOMBRE-USUARIO-")]]

    # for i in range(0,cant_car_mostrar):
    #     frame1.append(lista[i]) 

    [frame1.append(lista[i]) for i in range(0,cant_car_mostrar)]


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
          [sg.Text("Nombre data set",key="-NOMBRE-DATA-SET-")],
          #[sg.Text("Aca va una imagen",key="-IMAGEN-")],
          #[sg.Image(source=imagen,size=(200,150),key="-IMAGEN-")],
          [sg.Image(size=(50,50),key="-IMAGEN-")],
          [sg.Image(key="-IMAGEN-")],
          [sg.Frame("",frame1)],
          [sg.Button("Abandonar juego",key="-BOTON-ABANDONAR-JUEGO-")]
    ]

    col2=[
          [sg.Text("Dificultad:"),sg.Text("Aca va la dificultad",key="-DIFICULTAD-"),sg.Text("Puntaje actual:"),sg.Text("Aca va el puntaje",key="-PUNTAJE-")],
          [sg.Text("Tiempo:"),sg.Text("Aca va el tiempo",key="-TIEMPO-")],
          [sg.Frame("",frame2)],
    ]
    
    layout=[
            [sg.Column(col1),sg.Column(col2)]
    ]

    return sg.Window("FiguRace",layout=layout,margins=(100,100),finalize=True)

def traer_data_set(dataset):
    archivo_data_set=os.path.join(DATA_SETS_PATH,dataset)
    with open(archivo_data_set) as data_set:
        reader=csv.reader(data_set,delimiter=",") 
        header=list(next(reader))
        datos=list(reader)
    return header,datos
     

def cargar_caracteristicas_data_set(ventana,cant_car_a_mostrar,dataset):

    #traigo el dataset
    encabezado,datos=traer_data_set(dataset)
    #elijo un indice al azar para elegir un elemento al azar del dataset
    indice_dato_aleatorio=randint(0,len(datos)-1)
    dato_aleatorio=datos[indice_dato_aleatorio]
    print(dato_aleatorio)
    
    #renderizo los nombres de las caracteristicas con su respectiva caracteristica
    for i in range(cant_car_a_mostrar):
        ventana['-ETIQ-CAR-'+str(i)+'-'].Update(encabezado[i]+':')
        ventana['-CAR-'+str(i)+'-'].Update(dato_aleatorio[i])

    ventana["-ETIQ-CAR-ADIVINAR-"].Update(encabezado[-1]+':')    
    
    ventana["-IMAGEN-"].Update(size=(100,100),source=os.path.join(IMAGES_PATH,dataset.split('_')[0]+'.png'))

    #renderizo los botones 
    # elijo un boton al azar(del 1 al 5) y seteo la caracteristica que corresponde 
    numero_boton_opcion_correcta=randint(1,5)
    print('indice boton opcion correcta',numero_boton_opcion_correcta)
    ventana['-BOTON-'+str(numero_boton_opcion_correcta)+'-'].Update(dato_aleatorio[-1])
    indices_botones_restantes=[numero for numero in range(1,6) if numero != numero_boton_opcion_correcta]
    print(indices_botones_restantes)
    #completo los botones restantes con opciones al azar
    """aca no pude hacer el import =>"""
    indices_aleatorios=sample(range(0,len(datos)),4)
    #indices_aleatorios=[randint(0,len(datos)) for i in range(4)]
    print(indices_aleatorios)

    for boton,indice in zip(indices_botones_restantes,indices_aleatorios):
        print(datos[indice])  
        #ventana['-BOTON-'+str(boton)+'-'].Update(datos[indice][len(dato_aleatorio)-1])
        ventana['-BOTON-'+str(boton)+'-'].Update(datos[indice][-1])

    return numero_boton_opcion_correcta,indices_botones_restantes 


# #Generando estadisticas...   
# def generar_estadisticas(timestamp,id,evento,usuario,nivel,estado="",texto_ingresado="",respuesta=""):
#     archivo_estadisticas=os.path.join(ESTADISTICAS_PATH,'estadisticas.csv')
#     try:
#         # with open(archivo_estadisticas,'r') as arch_est:
#         #     reader=csv.reader(arch_est)
#         #     reader.__next__
#         #     datos=list(reader)    
#         # datos.append([timestamp,id,evento,usuario,estado,texto_ingresado,respuesta,nivel])
#         with open(archivo_estadisticas,'x') as arch_est:
#             writer=csv.writer(arch_est)    
#             writer.writerow([timestamp,id,evento,usuario,estado,texto_ingresado,respuesta,nivel])
#     except IOError:
#         encabezado=["timestamp","id","evento","usuario","estado","texto_ingresado","respuesta","nivel"]
#         with open(archivo_estadisticas,'w') as arch_est:
#             writer=csv.writer(arch_est)
#             writer.writerow(encabezado)
#             writer.writerow([timestamp,id,evento,usuario,estado,texto_ingresado,respuesta,nivel])
# 
def generar_puntajes(nombre_usuario,puntaje,dificultad):
    archivo_puntajes=os.path.join(PUNTAJES_PATH,'puntajes.json')
    try:
        with open(archivo_puntajes,'r') as arch_punt:
            dicc=json.load(arch_punt)
        if(dificultad in dicc.keys()):
            if(nombre_usuario in dicc[dificultad].keys()):    
                dicc[dificultad][nombre_usuario]={"puntaje":puntaje+dicc[dificultad][nombre_usuario]["puntaje"],"rondas_jugadas":dicc[dificultad][nombre_usuario]["rondas_jugadas"]+1}
            else:
                 dicc[dificultad][nombre_usuario]={"puntaje":puntaje,"rondas_jugadas":1}   
        else:
            dicc[dificultad]={nombre_usuario:{"puntaje":puntaje,"rondas_jugadas":1}}    
        with open(archivo_puntajes,'w') as arch_punt:
            json.dump(dicc,arch_punt,indent=4)    
    except IOError:
        dicc={}
        dicc[dificultad]={nombre_usuario:{"puntaje":puntaje,"rondas_jugadas":1}}
        with open (archivo_puntajes,'w') as arch_punt:
            json.dump(dicc,arch_punt,indent=4)


def generar_estadisticas(timestamp,id,evento,usuario,genero,nivel,estado="",texto_ingresado="",respuesta=""):
    archivo_estadisticas=os.path.join(ESTADISTICAS_PATH,'estadisticas.csv')
    if(os.path.exists(archivo_estadisticas)):
        with open(archivo_estadisticas,'a') as arch_est:
            writer=csv.writer(arch_est)    
            writer.writerow([timestamp,id,evento,usuario,genero,estado,texto_ingresado,respuesta,nivel])
    else:
        encabezado=["timestamp","id","evento","usuario","genero","estado","texto_ingresado","respuesta","nivel"]
        with open(archivo_estadisticas,'w') as arch_est:
            writer=csv.writer(arch_est)
            writer.writerow(encabezado)
            writer.writerow([timestamp,id,evento,usuario,genero,estado,texto_ingresado,respuesta,nivel])   

def ventana_juego(nombre,genero,dificultad,dicc_dificultad): 

    dataset_al_azar=lista_opciones_datasets[randint(0,1)]

    ventana_juego=crear_ventana_juego(dicc_dificultad["cant_rondas"])
    ventana_juego["-NOMBRE-USUARIO-"].Update(nombre)
    ventana_juego["-DIFICULTAD-"].Update(dificultad)
    ventana_juego["-NOMBRE-DATA-SET-"].Update(dataset_al_azar.split("_")[0].title())
    print(dicc_dificultad["cant_rondas"])
    numero_partida=uuid4()
    generar_estadisticas(int(time()),numero_partida,"inicio_partida",nombre,genero,dificultad)
    try:
        puntaje_actual=0
        ventana_juego["-PUNTAJE-"].Update(puntaje_actual)
        
        for i in range(0,dicc_dificultad["cant_rondas"]):
            ventana_juego["-TIEMPO-"].Update(dicc_dificultad["tiempo"])
            print(i)
            hora_inicial=time()
            numero_boton_opcion_correcta,indices_botones_restantes=cargar_caracteristicas_data_set(ventana_juego,dicc_dificultad["cant_car_mostrar"],dataset_al_azar)
            lista_opciones_incorrectas=list(map(lambda i:'-BOTON-'+str(i)+'-',indices_botones_restantes))
            #timestamp,id,evento,usuario,nivel,estado="",texto_ingresado="",respuesta=""):
            while True:
                event,values=ventana_juego.read(timeout=250)

                transcurridos=int(time()-hora_inicial)
                restantes=int(dicc_dificultad["tiempo"].strip("s"))-transcurridos
                ventana_juego["-TIEMPO-"].Update(f"00:{restantes}s")

                if(event in (None,"-BOTON-ABANDONAR-JUEGO-")):
                    raise AbandonarJuegoExcepcion()
                elif(event=='-BOTON-'+str(numero_boton_opcion_correcta)+'-'):
                    estado="ok"
                    ventana_juego[f"-RESPUESTA-{i+1}"].Update("CORRECTO",text_color="green")
                    puntaje_actual+=dicc_dificultad["punt_sum_resp"]
                    ventana_juego["-PUNTAJE-"].Update(puntaje_actual)
                    generar_estadisticas(int(time()),numero_partida,"intento",nombre,genero,dificultad,estado,ventana_juego[event].ButtonText,ventana_juego[event].ButtonText)
                    break
                elif(event in lista_opciones_incorrectas):
                    estado="error"
                    ventana_juego[f"-RESPUESTA-{i+1}"].Update("INCORRECTO",text_color="red")
                    puntaje_actual-=dicc_dificultad["punt_res_resp"]
                    ventana_juego["-PUNTAJE-"].Update(puntaje_actual)
                    sg.Popup('La respuesta correcta es:'+ventana_juego['-BOTON-'+str(numero_boton_opcion_correcta)+'-'].ButtonText)
                    generar_estadisticas(int(time()),numero_partida,"intento",nombre,genero,dificultad,estado,ventana_juego[event].ButtonText,ventana_juego['-BOTON-'+str(numero_boton_opcion_correcta)+'-'].ButtonText)
                    break    
                elif(event=="-BOTON-PASAR-"):
                    estado="pasó"
                    ventana_juego[f"-RESPUESTA-{i+1}"].Update("PASÓ")
                    puntaje_actual-=dicc_dificultad["punt_res_resp"]
                    ventana_juego["-PUNTAJE-"].Update(puntaje_actual)
                    generar_estadisticas(int(time()),numero_partida,"intento",nombre,genero,dificultad,estado,respuesta=ventana_juego['-BOTON-'+str(numero_boton_opcion_correcta)+'-'].ButtonText)
                    break
                elif(restantes==0):
                    estado="timeout"
                    ventana_juego[f"-RESPUESTA-{i+1}"].Update("INCORRECTO",text_color="red")
                    puntaje_actual-=dicc_dificultad["punt_res_resp"]
                    ventana_juego["-PUNTAJE-"].Update(puntaje_actual)
                    generar_estadisticas(int(time()),numero_partida,"intento",nombre,genero,dificultad,estado,respuesta=ventana_juego['-BOTON-'+str(numero_boton_opcion_correcta)+'-'].ButtonText)
                    break
        generar_puntajes(nombre,puntaje_actual,dificultad)

        #ventana_juego.close()
    except AbandonarJuegoExcepcion:
        generar_estadisticas(int(time()),numero_partida,"fin",nombre,genero,dificultad,"cancelada")
        ventana_juego.close()
    else:
        generar_estadisticas(int(time()),numero_partida,"fin",nombre,genero,dificultad,"finalizada")
        sg.Popup(f"El puntaje final es:{puntaje_actual}")
        ventana_juego.close()                              

