import os,csv 

DATA_SETS_FILE=os.path.abspath(os.path.join(__file__,'..','..','data_sets'))
archivo_lagos=os.path.join(DATA_SETS_FILE,'Lagos Argentina .csv')

DATA_SETS_PROCESADOS_FILE= os.path.abspath(os.path.join(__file__,'..','..','data_sets_procesados'))
#print(DATA_SETS_PROCESADOS_FILE)
archivo_lagos_procesado=os.path.join(DATA_SETS_PROCESADOS_FILE,'lagos_argentina_procesado.csv')

def pasar_a_grados(lista):
   #aca me llega como parametro algo del estilo:["54 34 66","78 32 12"] 
   lista_en_grados=map(lambda x:str(round(int(x[0])+int(x[1])/60+int(x[2])/3600,2)),
   map(lambda x:x.split(" "),lista))
   return list(lista_en_grados)   

def limpiar_coordenadas(lago):
   #tomo las coordenadas para trabajar y las separo
   coord=lago[5].split(" ")
   #saco los caracteres que no sirven
   coord_limpias=map(lambda x:x.replace("°"," ").replace("'"," ").replace("\"","").
   replace("S","").replace("O","").strip(),coord)
   #me apoyo en otra funcion para convertir a grados
   coord_en_grados=pasar_a_grados(coord_limpias) #aca tengo algo como:["54.23","77.45"]
   #le doy formato y obtengo algo como:"54.23°S 77.45°O"
   coord_finales=coord_en_grados[0]+"°S"+" "+coord_en_grados[1]+"°O"
   return coord_finales
   #lago[5]=coord_finales
   #return lago      


#ruta_archivos="data_sets"
#ruta_completa = os.path.join(os.getcwd(), ruta_archivos)
#archivo_lagos=os.path.join(ruta_completa,"Lagos Argentina .csv")
#archivo_lagos_procesado=os.path.join(ruta_completa,"lagos_argentina_procesado.csv")

try:
   with open(archivo_lagos,encoding="utf-8") as data_set:
      reader=csv.reader(data_set,delimiter=",") 
      header=list(next(reader))
      todos_lagos=list(reader)
   print(header)
   nombre=header[0]
   header_temp=header[1:]
   header_temp.append(nombre)
   header_final=header_temp
   # todos_lagos=list(reader)
   #print('Los lagos sin procesar son:',todos_lagos,'aca terminan...')
   lagos_procesados=[]
   for lago in todos_lagos:
      if(lago[3]=='' or lago[4]==''):
         lago[3]='Desconocido'
         lago[4]='Desconocido'
      #en la posicion cinco pongo las coordenadas procesadas
      lago[5]=limpiar_coordenadas(lago)
      #me guardo el nombre para despues pasarlo al ultimo lugar
      nombre_lago=lago[0]
      #tomo desde la posicion 1 hasta el final
      lago_final=lago[1:]
      #agrego el nombre a lo ultimo
      lago_final.append(nombre_lago)
      #agrego el lago a la lista de lagos procesados
      lagos_procesados.append(lago_final)
      #print(lago)
      #lagos_procesados.append(limpiar_coordenadas(lago))
      #nombre=lago[0]
      #lago_temp=lago[1:]
      #lago_temp.append(limpiar_coordenadas(lago))
   print('Los lagos procesados son:',lagos_procesados,'aca terminan...')
   with open(archivo_lagos_procesado,"w") as salida:
      writer=csv.writer(salida)
      writer.writerow(header_final)
      writer.writerows(lagos_procesados)     
except(IOError):
   print("No se encontro el archivo")     



      


