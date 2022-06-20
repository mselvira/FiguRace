from functools import reduce
import os,csv
#from functools import reduce 

DATA_SETS_FILE=os.path.abspath(os.path.join(__file__,'..','..','data_sets'))
archivo_fifa=os.path.join(DATA_SETS_FILE,'FIFA-21 Complete.csv')

DATA_SETS_PROCESADOS_FILE= os.path.abspath(os.path.join(__file__,'..','..','data_sets_procesados'))
#print(DATA_SETS_PROCESADOS_FILE)
archivo_fifa_procesado=os.path.join(DATA_SETS_PROCESADOS_FILE,'fifa_procesado.csv')

def modificar_posiciones(jugador):
    dicc_posiciones={
       "GK":"Arquero","SW":"Libero","LB":"Left back","LCB":"Left Centre Back","CB":"Centre Back","RCB":"Right Centre Back","RB":"Right Back","LWB":"Left Wing Back","LDM":"Left Defensive Midfielder","CDM":"Centre Defensive Midfielder","RDM":"Right DEfensive Midfielder","RWB":"Right Wing Back","LM":"Left Midfielder","LCM":"Left Centre Midfielder","CM":"Centre Midfielder","RCM":"Right Centre Midfielder","RM":"Right Midfielder","LAM":"Left Attacking Midfielder","CAM":"Centre Attacking Midfielder","RAM":"Right Attacking Midfielder","LW":"Left Wing","RW":"Right Wing","LS":"Left Striker","CF":"Centre Forward","RS":"Rigth Sriker","SS":"Second Striker","ST":"Striker"
   }
    siglas_de_posiciones=jugador[3].split("|")
    #posiciones=[dicc_posiciones[pos] for pos in dicc_posiciones.items()]
    posiciones=list(map(lambda x:dicc_posiciones[x],siglas_de_posiciones))
    print(posiciones)
    jugador[3]='|'.join(posiciones)
    #jugador[3]=reduce(lambda x,y='|':dicc_posiciones[x]+y,siglas_de_posiciones)
    print("****",jugador)

# Regular: Menos de 60
# Bueno: Entre 60 y 79 (inclusive)
# Muy bueno: Entre 80 y 89 (inclusive)
# Sobresaliente: Desde 90 en adelante    

def reemplazar_potencial(jugador):
   potencial=jugador[7]
   if(potencial in range(0,60)):
      jugador[7]="Regular"
   elif(potencial in range(60,80)):
      jugador[7]="Bueno"
   elif(potencial in range(80,90)):
      jugador[7]="Muy bueno"
   else:
      jugador[7]="Sobresaliente"
   print(jugador)    
                
    

try:
   with open(archivo_fifa,"r",encoding="utf-8") as data_set:
      reader=csv.reader(data_set,delimiter=";") 
      header=list(next(reader))
      jugadores=list(reader)
   # print(header)
   # print(jugadores[9])
   # modificar_posiciones(jugadores[9])
   # reemplazar_potencial(jugadores[9])
   #jugadores_posiciones_procesadas=map(modificar_posiciones,jugadores)
   #print(type(jugadores_posiciones_procesadas))
   jugadores=list(map(reemplazar_potencial,map(modificar_posiciones,jugadores)))
   print(jugadores)   
except(IOError):
    print("No se encontro el archivo")      