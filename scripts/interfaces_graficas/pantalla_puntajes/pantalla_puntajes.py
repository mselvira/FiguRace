import PySimpleGUI as sg

def crear_ventana_puntajes():
    layout=[ 
             [sg.Button("Volver al menu de inicio",key="-VOLVER-MENU-INICIO-")]
    ]
    return sg.Window("",layout=layout,margins=(100,100)) 


def ventana_puntajes():
    
    vent_puntajes=crear_ventana_puntajes()
    event,values=ventana_puntajes.read()
    while True:
        if(event in(None,"-VOLVER-MENU-INICIO-")):
            vent_puntajes.close()
