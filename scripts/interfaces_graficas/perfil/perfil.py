import json
import PySimpleGUI as sg 
import os

ARCHIVOS_FIGURACE = os.path.abspath(os.path.join(__file__, '..', '..','..','..','archivos_figurace'))
archivo_perfiles=os.path.join(ARCHIVOS_FIGURACE, 'perfiles.json')

def crear_ventana_perfil(): 
    
    layout=[
            [sg.Text("Cree o edite su perfil",justification="center",expand_x=True)],
            [sg.Input("Ingrese su nombre",justification="center",expand_x=True,key="-NOMBRE-")],
            [sg.Input("Ingrese su edad",justification="center",expand_x=True,key="-EDAD-")],
            [sg.Input("Ingrese su genero autopercibido",justification="center",expand_x=True,key="-GENERO-")],
            [sg.Button("Crear perfil",key="-BOTON-CREAR-PERFIL-"),sg.Button("Editar perfil",key="-BOTON-EDITAR-PERFIL-")],
            [sg.Button("Volver al menu de inicio",key="-VOLVER-MENU-INICIO-")] 
    ]
    
    return sg.Window("Creacion del perfil de usuario",layout,size=(500,500))

def algun_campo_vacio(dicc):
    return dicc["-NOMBRE-"]=="" or dicc["-EDAD-"]=="" or dicc["-GENERO-"]==""

def crear_perfil(values,claves):
    lista_dic=[]
    try:
        with open(archivo_perfiles,"r",encoding="utf-8") as archivo:
           lista_dic=json.load(archivo)
        nombres=[dic["Nombre"] for dic in lista_dic]            
        if(values["-NOMBRE-"] in nombres):
            sg.Popup(f'No es posible crear el perfil porque ya existe un usuario registrado con el nombre:{values["-NOMBRE-"]}')
        else:
            #dic={"Nombre":values["-NOMBRE-"],"Edad":values["-EDAD-"],"Genero":values["-GENERO]}-"
            dic={clave:valor for clave,valor in zip(claves,values.values())}
            lista_dic.append(dic) 
            with open(archivo_perfiles,"w",encoding="utf-8") as archivo:               
                json.dump(lista_dic,archivo,indent=4)
            sg.Popup("Perfil creado correctamente")     
            #print(nombres)           
    except IOError:
        #dic={"Nombre":values["-NOMBRE-"],"Edad":values["-EDAD-"],"Genero":values["-GENERO-"]}
        dic={clave:valor for clave,valor in zip(claves,values.values())}
        lista_dic.append(dic) 
        with open(archivo_perfiles,"w",encoding="utf-8") as archivo: 
            json.dump(lista_dic,archivo,indent=4)
        sg.Popup("Perfil creado correctamente") 

def editar_perfil(values):
    try:
        with open(archivo_perfiles,"r",encoding="utf-8") as archivo:
            lista_dic=json.load(archivo)
    except:
        sg.Popup("No se pudo editar el perfil porque aun no hay perfiles creados")
    else:
        nombres=[dic["Nombre"] for dic in lista_dic]             
        if(not values["-NOMBRE-"] in nombres):
            sg.Popup(f'No es posible la edicion del perfil porque no existe un usuario registrado con el nombre:{values["-NOMBRE-"]}')   
        else:
            indice=nombres.index(values["-NOMBRE-"])
            lista_dic[indice]["Edad"]=values["-EDAD-"]
            lista_dic[indice]["Genero"]=values["-GENERO-"]
            with open(archivo_perfiles,"w",encoding="utf-8") as archivo:
                json.dump(lista_dic,archivo,indent=4)
            sg.Popup("Perfil editado correctamente")               
       
def ventana_perfil():  
    claves=["Nombre","Edad","Genero"]  
    ventana_perfil=crear_ventana_perfil()
    while True:
        event,values=ventana_perfil.read()
        if(event in (None,"-VOLVER-MENU-INICIO-")):
            break
        elif(event=="-BOTON-CREAR-PERFIL-"):
            if(algun_campo_vacio(values)):
                sg.Popup("Hay algun campo sin completar,por favor completa todos los campos")
            else:
                crear_perfil(values,claves)      
        elif(event=="-BOTON-EDITAR-PERFIL-"):    
            if(algun_campo_vacio(values)):
                sg.Popup("Hay algun campo sin completar,por favor completa todos los campos")
            else:
                editar_perfil(values)
    ventana_perfil.close() 
       
