from math import log10, sqrt
import cv2
# para instalar la libreria openCV simplemente:
# pip3 install opencv-python
# o bien py -m pip install opencv-python
# para aprender opencv https://www.geeksforgeeks.org/opencv-python-tutorial
import numpy as np
import os
from pathlib import Path
import time
#para instalar el modulo easygui simplemente:
#pip3 install easygui
# o bien py -m pip install easygui

#import easygui
from tkinter import messagebox
import lock
import json

# variables globales
# ------------------
props_dict={}
DEBUG_MODE=True

def init(props):
    global props_dict
    print("Python: Enter in init")
    
    #props es un diccionario
    props_dict= props
    
    # retornamos un cero como si fuese ok, porque
    # no vamos a ejecutar ahora el challenge
    return 0 # si init va mal retorna -1 else retorna 0
    

def executeChallenge():
    print("Starting execute")
    #for key in os.environ: print(key,':',os.environ[key]) # es para ver variables entorno
    folder=os.environ['SECUREMIRROR_CAPTURES']
    print ("storage folder is :",folder)
    
    # mecanismo de lock BEGIN
    # -----------------------
    lock.lockIN("ENVIRONMENT")

    # pregunta si el usuario tiene movil con capacidad foto
    # -----------------------------------------------------
    #textos en español, aunque podrian ser parametros adicionales del challenge
    #capable=easygui.ynbox(msg='¿Tienes un movil con bluetooth activo y emparejado con tu PC con capacidad GPS?', choices=("Yes","Not"))
    capable=messagebox.askyesno('challenge MM: RGB','¿Tienes un movil con bluetooth activo emparejado a tu PC con capacidad environment?')
    
    print (capable)

    if (capable==False):
        lock.lockOUT("ENVIRONMENT")
        print ("return key zero and long zero")
        key=0
        key_size=0
        result =(key,key_size)
        print ("result:",result)
        return result # clave cero, longitud cero
    
    #popup msgbox pidiendo interaccion
    #---------------------------------
    #output = easygui.msgbox(props_dict["interactionText"], "challenge MM: ENVIRONMENT")
    output = messagebox.showinfo("challenge MM: ENVIRONMENT",props_dict["interactionText"])

    
    
    # lectura del fichero capture.geo
    #-------------------------------
    # se supone que el usuario ha depositado un .geo usando bluetooth
    # el nombre del fichero puede ser siempre el mismo, fijado por el proxy bluetooth.
    # aqui vamos a "forzar" el nombre del fichero para pruebas
    filename="capture.env"
    if (DEBUG_MODE==True):
        filename="test.env"

    if os.path.exists(folder+"/"+filename):    
        with open(folder+"/"+filename) as cosa:
            envdata=json.load(cosa)
            print (envdata)
    else:
        print ("ERROR: el fichero de captura",filename," no existe")
        key=0
        key_size=0
        result =(key,key_size)
        print ("result:",result)
        lock.lockOUT("ENVIRONMENT")
        return result # clave cero, longitud cero
    
   

    
    # una vez consumida, podemos borrar la captura (fichero "capture.geo")
    if (DEBUG_MODE==False):
        if os.path.exists(folder+"/"+filename):    
            os.remove(folder+"/"+filename)
        
    
    
    #mecanismo de lock END
    #-----------------------
    lock.lockOUT("ENVIRONMENT")
    
    #procesamiento
    # averigua si la altura esta en un rango concreto
    temp=envdata["temperature"] # primera toma de GPS, componente alt
    cuantized_temp=float(temp)
    cuantized_temp=int(temp/5.0)
    
    hum=envdata["humidity"]
    cuantized_hum=int(float(hum/10.0)) 

    oz=envdata["ozone"]
    cuantized_oz=int(float(oz/3.0))
    
    print ("temp es ", cuantized_temp)
    print ("humidity es ", cuantized_hum)
    print ("ozone es ", cuantized_oz)
    

    #construccion de la respuesta
    cad="%d%d%d"%(cuantized_temp, cuantized_hum, cuantized_oz)
    key = bytes(cad,'utf-8')
    key_size = len(key)
    result =(key, key_size)
    print ("result:",result)
    return result


if __name__ == "__main__":
    midict={"interactionText": "Por favor haz una captura de datos de environment", "param2":3}
    init(midict)
    executeChallenge()

