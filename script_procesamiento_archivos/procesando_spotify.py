import csv,os

DATA_SETS_FILE=os.path.abspath(os.path.join(__file__,'..','..','data_sets'))
archivo_canciones=os.path.join(DATA_SETS_FILE,'Spotify 2010 - 2019 Top 100.csv')

DATA_SETS_PROCESADOS_FILE= os.path.abspath(os.path.join(__file__,'..','..','data_sets_procesados'))
#print(DATA_SETS_PROCESADOS_FILE)
archivo_spotify_procesado=os.path.join(DATA_SETS_PROCESADOS_FILE,'spotify_procesado.csv')

def formatear_genero(cancion):
    siglas=["edm","dfw","uk","r&b","lgbtq+"]
    palabras=cancion[2].split(" ",1)
    if(palabras[0] in siglas):
        palabras[0]=palabras[0].upper()
    elif(palabras[0]=="k-pop"):
        palabras[0]="K-Pop"
    else:
        palabras[0]=palabras[0].capitalize()    
    if(len(palabras)>1):    
        palabras[1]=palabras[1].title()    
    genero_final=" ".join(palabras)
    #cancion[2]=genero_final
    return genero_final

#ruta_archivos="data_sets"
#ruta_completa = os.path.join(os.getcwd(), ruta_archivos)
#archivo_canciones=os.path.join(ruta_completa,"Spotify 2010 - 2019 Top 100.csv")
#archivo_spotify_procesado=os.path.join(ruta_completa,"spotify_procesado.csv")

try:
   with open(archivo_canciones,encoding="utf-8") as data_set:
      reader=csv.reader(data_set,delimiter=",")
      header=list(next(reader))
      header_final=[]   
      header_final.append(header[2])
      header_final.append(header[len(header)-1])
      header_final.append(header[3])
      header_final.append(header[len(header)-2])
      header_final.append(header[5])
      header_final.append(header[1]) 
      canciones=list(reader)
      canciones_procesadas=[]
      print(len(canciones))
      print(header_final)
      for cancion in canciones:
          cancion_final=[]
          cancion_final.append(formatear_genero(cancion))
          cancion_final.append(cancion[len(cancion)-1])
          cancion_final.append(cancion[3])
          cancion_final.append(cancion[len(cancion)-2])
          cancion_final.append(cancion[5])
          cancion_final.append(cancion[1])
          canciones_procesadas.append(cancion_final)  
      for cancion in canciones_procesadas:
          print(cancion)
      with open(archivo_spotify_procesado,"w") as salida:
          writer=csv.writer(salida)
          writer.writerow(header_final)
          writer.writerows(canciones_procesadas)               
except(IOError):
   print("No se encontro el archivo")
   
