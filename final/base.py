#!/usr/bin/env python
# encoding: utf-8
#from time import gmtime, strftime
import StringIO
import sys
import os
import threading
from threading import Thread
import time
import multiprocessing 
from multiprocessing import Process, Queue
import signal
import random
from socket import socket, AF_INET, SOCK_STREAM

#metodo limpiar pantalla http://stackoverflow.com/questions/517970/how-to-clear-python-interpreter-console
def cls():
    os.system(['clear','cls'][os.name == 'nt'])

#Clase generica. Se asumió que todos los procesos tienen tiempo (ver proceso 5)
class Proceso:

    #Inicializa la clase
    def __init__(self,nombre,fecha,tipo,prioridad,tiempo):
        self.nombre=nombre  
        self.fecha=int(fecha)
        self.tipo=int(tipo)
        self.prioridad=int(prioridad)
        self.tiempo=int(tiempo)
        self.tiempoTotal=int(tiempo)
        
        #v 2.3 lista de perifericos
        self.listperi = []

    #getters
    def getNombre(self):
        return self.nombre
    def getFecha(self):
        return self.fecha
    def getTipo(self):
        return self.tipo
    def getPrioridad(self):
        return self.prioridad
    def getTiempo(self):
        return self.tiempo
    def getTiempoTotal(self):
        return self.tiempoTotal
    def getListperi(self, i):
        return self.listperi[i]
    def decTiempo(self):
        self.tiempo -= 1
        return
    def texto(self):
        if(self.tipo == 1):
            return "Se hizo una llamada al número %d que se demoró %d segundos." %(self.numero, self.tiempoTotal)
        elif(self.tipo == 2):
            return "Se recibió una llamada del número %d que se demoró %d segundos." %(self.numero, self.tiempoTotal)
        elif(self.tipo == 3):
            return "Se envió el siguiente mensaje al número %d : %s . Enviarlo se demoró %d segundos." %(self.numero, self.txt, self.tiempoTotal)
        elif(self.tipo == 4):
            return "Se recibió el siguiente mensaje del número %d : %s . Recibirlo se demoró %d segundos." %(self.numero, self.txt, self.tiempoTotal)
        elif(self.tipo == 5):
            return "Se agregó a %s en la agenda de contactos y su número es %d ." %(self.nombre_contacto, self.numero_contacto)
        elif(self.tipo == 6):
            return "Se ejecutó un proceso que duró %d segundos." %(self.tiempoTotal)
        elif(self.tipo == 7):
            return "Se mandó la ubicación, proceso que tomó dos segundos."
        elif(self.tipo == 8):
            return "Se vió la ubicación, proceso que tomó %d segundos." % (self.tiempoTotal)
        elif(self.tipo == 9):
            return "Se se jugó durante %d segundos." % (self.tiempoTotal)
        elif(self.tipo == 10):
            return "Se escuchó música por %d segundos." % (self.tiempoTotal)
        else:
            return "Se intentó ejecutar un proceso inexistente. No nos ponga a prueba."
        
        
        
        
    #Funcion texto, entrega un string para guardar en la memoria (el archivo)
        

#Clase Llamada que hereda de proceso
class Llamada(Proceso):

    #Inicializador de la llamada. Recibe el texto de input y genera la llamada
    def __init__(self, texto_proceso):
        global tiempo_ejecucion
        
        arreglo=texto_proceso.split(';')
        if arreglo[1]!='-1':
            Proceso.__init__(self,arreglo[0],arreglo[1],arreglo[2],arreglo[3],arreglo[5])
        else:
            Proceso.__init__(self,arreglo[0],tiempo_ejecucion,arreglo[2],arreglo[3],arreglo[5])
        self.numero=int(arreglo[4])
        #v 2.3
        self.listperi.append(1)
        self.listperi.append(3)
        self.listperi.append(3)
        self.listperi.append(0)
        self.listperi.append(1)
        self.listperi.append(1)
        
    #Aqui van los metodos que se le quieran añadir
        
class Mensaje(Proceso):
    def __init__(self, texto_proceso):
        global tiempo_ejecucion
        arreglo=texto_proceso.split(';')
        if arreglo[1]!='-1':
            Proceso.__init__(self,arreglo[0],arreglo[1],arreglo[2],arreglo[3],0.02*len(arreglo[5])+1)
        else:
            Proceso.__init__(self,arreglo[0],tiempo_ejecucion,arreglo[2],arreglo[3],0.02*len(arreglo[5])+1)
        self.numero=int(arreglo[4])
        self.txt=arreglo[5]
        self.listperi.append(0)
        self.listperi.append(1)
        self.listperi.append(0)
        self.listperi.append(0)
        self.listperi.append(1)
        self.listperi.append(1)

     #Agregar metodos



class Agregar_Contacto(Proceso):
    def __init__(self, texto_proceso):
        global tiempo_ejecucion
        arreglo=texto_proceso.split(';')
        if arreglo[1]!='-1':
            Proceso.__init__(self,arreglo[0],arreglo[1],arreglo[2],arreglo[3],1)
        else:
            Proceso.__init__(self,arreglo[0],tiempo_ejecucion,arreglo[2],arreglo[3],1)
        self.nombre_contacto=arreglo[4]
        self.numero_contacto=int(arreglo[5])
        self.listperi.append(1)
        self.listperi.append(0)
        self.listperi.append(0)
        self.listperi.append(0)
        self.listperi.append(0)
        self.listperi.append(0)
        
    def numero_contacto(self):
        return self.numero_contacto 
    #Agregar metodos
    



        
#Cualquiera, ubicacion, ver y mandar ubicacion, jugar y musica
class Varios(Proceso):
    def __init__(self, texto_proceso):
        arreglo=texto_proceso.split(';')
        #Se evalua si es mandar ubicacion o no
        if arreglo[2] == "7":
            self.listperi.append(0)
            self.listperi.append(0)
            self.listperi.append(0)
            self.listperi.append(1)
            self.listperi.append(1)
            self.listperi.append(0)
            if arreglo[1]!='-1':
                Proceso.__init__(self,arreglo[0],arreglo[1],arreglo[2],arreglo[3],2)
            else:
                Proceso.__init__(self,arreglo[0],tiempo_ejecucion,arreglo[2],arreglo[3],2)
        else:
            if arreglo[1]!='-1':
                Proceso.__init__(self,arreglo[0],arreglo[1],arreglo[2],arreglo[3],arreglo[4])
            else:
                Proceso.__init__(self,arreglo[0],tiempo_ejecucion,arreglo[2],arreglo[3],arreglo[4])
        #v 2.3 
        if arreglo[2] == "6":
            self.listperi.append(2)
            self.listperi.append(1)
            self.listperi.append(1)
            self.listperi.append(1)
            self.listperi.append(1)
            self.listperi.append(1)
        if arreglo[2] == "8":
            self.listperi.append(1)
            self.listperi.append(0)
            self.listperi.append(0)
            self.listperi.append(1)
            self.listperi.append(0)
            self.listperi.append(0)
        if arreglo[2] == "9":
            self.listperi.append(2)
            self.listperi.append(1)
            self.listperi.append(0)
            self.listperi.append(1)
            self.listperi.append(1)
            self.listperi.append(1)
        if arreglo[2] == "10":
            self.listperi.append(1)
            self.listperi.append(1)
            self.listperi.append(0)
            self.listperi.append(0)
            self.listperi.append(0)
            self.listperi.append(0)
        #Agregar metodos

        
#Clase representando el proceso que se esta ejecutando      
class Simulador:
    
    #Inicializador de la ejecución de los procesos
    def __init__(self):
        pass
        
    #v 2.3 metodo que updatea la lista de los perifericos que estan siendo utilizados
    def updatePerifericos(self):
        global perifericos
        perifericos = []
        for x in range(0,6):
            perifericos.append(0)
        for p in range (0, len(running)):
            for x in range(0, 6):
                if(running[p].getListperi(x) > perifericos[x]):
                    perifericos[x] = running[p].getListperi(x)
                
        
    #Función que simula los procesos, proceso_andando es el numero
    def Simular(self):
        global disp
        global top
        global tiempo_ejecucion
        global running
        global ready
        global procesos
        global seguir
        #v2.3
        global perifericos
        perifericos = []
        for x in range(0,6):
            perifericos.append(0)
        cambioperif = False
        
        disp = Display()
        boolean = top
         
        while(seguir):
            
            #v 2.3 ejecutar simulacion, haciendo que pase el tiempo en los procesos
            if (running != None):
                for r in running:
                    #print running.texto()
                    r.decTiempo()
                    #acá se graba en memoria cuando el proceso termina 
                    if(r.getTiempo() <= 0):
                        memoria.escribir_memoria(r)
                        running.remove(r)
                        self.updatePerifericos()
                        cambioperif = True
                    
            #v 2.3 procesos que llegan al momento actual en la simulacion
            if(len(procesos) > 0 and procesos[0].fecha == tiempo_ejecucion):
            #for que revisa solo los procesos que les toca ejecutarse
                x = 0
                y = len(procesos)
                while (x < y):
                #for que revisa los perifericos que pueden necesitar o bloquear
                    for r in range (0, 3):
                        #caso 1: actualmente esta bloqueado un periferico y el proceso entrante usa ese periferico
                        if(perifericos[r] == 3 and procesos[x].getListperi(r) != 0):
                            ready.append(procesos.pop(x))
                            ready = sorted(ready, key=lambda procesos: procesos.prioridad)
                            break
                        #caso 2: actualmente esta necesitado primer periferico y el proceso entrante usa ese periferico
                        elif(perifericos[r] == 2 and procesos[x].getListperi(r) != 0):
                            for n in range (0, len(running)):
                                if(running[n].getListperi(0) == 2):
                                    if(running[n].getPrioridad < procesos[x].getPrioridad):
                                        ready.append(procesos.pop(x))
                                        ready = sorted(ready, key=lambda procesos: procesos.prioridad)
                                        break
                                    else:
                                        ready.append(running.pop(n))
                                        ready = sorted(ready, key=lambda procesos: procesos.prioridad)
                                        running.append(procesos.pop(x))
                                        self.updatePerifericos()
                                        cambioperif = True
                                        break
                            break
                        #caso 3: proceso entrante necesita o bloquea periferico, pero este a lo mas esta siendo usado
                        elif(procesos[x].getListperi(r) > 1):
                            if(perifericos[r] == 1):
                                maxprioridad = 666
                                for n in range (0, len(running)):
                                    if(running[n].getPrioridad < maxprioridad):
                                        maxprioridad = running[n].getPrioridad
                                if(maxprioridad < procesos[x].getPrioridad ):
                                    ready.append(procesos.pop(x))
                                    ready = sorted(ready, key=lambda procesos: procesos.prioridad)
                                    break
                                else:
                                    for n in range (0, len(running)):
                                        if(running[n].getListperi(r) > 0):
                                            ready.append(running.pop(n))
                                            ready = sorted(ready, key=lambda procesos: procesos.prioridad)
                                    running.append(procesos.pop(x))
                                    self.updatePerifericos()
                                    cambioperif = True
                                    break
                                break
                    #caso 4: que el proceso entrante no topa con ningun periferico bloqueado o necesitado
                    else:
                        running.append(procesos.pop(x))
                        self.updatePerifericos()
                        cambioperif = True
                    #ve si el proximo proceso no se va a ejecutar
                    if(len(procesos)>1):
                        if(procesos[x+1].fecha != tiempo_ejecucion):
                            break
                    x += 1
                    y = len(procesos)
            
            # v 2.3 revisa en la cola ready si puede entrar alguno después de que llegaron procesos o de que terminaron procesos
            if(cambioperif):
                self.updateReady()
            
            #v 2.3 display final del segundo de ejecucion
            disp.actualizar_ejecucion(boolean)
            
            boolean = top
            cambioperif = False
            time.sleep(1)
            tiempo_ejecucion += 1
            #limpia la pantalla
            cls()
            print "Comandos:\n'salir'-> detiene programa\n'top'-> ver procesos (2 veces deja de ver los procesos)\n'nombre_proc;tipo;opc1;opc2sihay'-> ingresa un nuevo proceso\n'menu_sockets'-> menu para conectar con otro dispositivo\nTiempo actual:"+ str(tiempo_ejecucion)
            
    def updateReady(self):
        global disp
        global top
        global running
        global ready
        #v2.3
        global perifericos
    # v 2.3 revisa en la cola ready si puede entrar alguno después de que llegaron procesos o de que terminaron procesos
        if(True):
            x = 0
            y = len(ready)
            while (x < y):
            #for que revisa los perifericos que pueden necesitar o bloquear
                for r in range (0, 3):
                    #caso 1: actualmente esta bloqueado un periferico y el proceso en running que intenta entrar usa ese periferico
                    if(perifericos[r] == 3 and ready[x].getListperi(r) != 0):
                        break
                    #caso 2: actualmente esta necesitado primer periferico y el proceso en running que intenta entrar usa ese periferico
                    elif(perifericos[r] == 2 and ready[x].getListperi(r) != 0):
                        for n in range (0, len(running)):
                            if(running[n].getListperi(0) == 2):
                                if(running[n].getPrioridad <= ready[x].getPrioridad):
                                    break
                                else:
                                    running.append(ready.pop(x))
                                    ready.append(running.pop(n))
                                    ready = sorted(ready, key=lambda procesos: procesos.prioridad)
                                    self.updatePerifericos()
                                    break
                        break
                    #caso 3: proceso entrante necesita o bloquea periferico, pero este a lo mas esta siendo usado
                    elif(ready[x].getListperi(r) > 1):
                        if(perifericos[r] == 1):
                            maxprioridad = 666
                            for n in range (0, len(running)):
                                if(running[n].getPrioridad < maxprioridad):
                                    maxprioridad = running[n].getPrioridad
                            if(maxprioridad <= ready[x].getPrioridad):
                                break
                            else:
                                for n in range (0, len(running)):
                                    if(running[n].getListperi(r) > 0):
                                        ready.append(running.pop(n))
                                        ready = sorted(ready, key=lambda procesos: procesos.prioridad)
                                running.append(ready.pop(x))
                                self.updatePerifericos()
                                break
                            break           
                #caso 4: que el proceso entrante no topa con ningun periferico bloqueado o necesitado
                else:
                    running.append(ready.pop(x))
                    self.updatePerifericos()
                x += 1
                y = len(ready)

#Clase que escribe en pantalla los procesos      
class Display():
    def actualizar_ejecucion(self, top):
        global running
        global ready
        global tiempo_ejecucion
        global perifericos
        
        numero = "10"
        r = len(running)
        
        if (top and r > 0):
            print "Actual Tasks: \n"
            print "Process\t\tTime of arrival\t\tPriority\t\tTime remaining\n"
            for w in running:
                print  str(w.nombre) + "\t\t" + str(w.fecha) + "\t\t" + str(w.prioridad) + "\t\t" + str(w.tiempo) + "\n"     
            print "Tasks: " + str(r) + " running\n"
            print "----------------\n\n"
        
        if (top and len(ready) > 0):
            print 'Cola ready :\n'
            for x in ready: 
                print "Ready Tasks: " + str(x.nombre) + ", Time of arrival: " + str(x.fecha) + ", Priority: " + str(x.prioridad)
        
        def dicper(x):
            if x == 0:
                return 'Pantalla: '
            elif x == 1:
                return 'Audifono: '
            elif x == 2:
                return 'Microfono: '
            elif x == 3:
                return 'GPS: '
            elif x == 4:
                return 'Enviar Info.: '
            elif x == 5:
                return 'Recibir Info.: '
            
        def dicestado(x):
            if x == 0:
                return 'Libre'
            elif x == 1:
                return 'En uso'
            elif x == 2:
                return 'Necesitado'
            elif x == 3:
                return 'Bloqueado'
                
        if (top):
            print "\nEl estado de los perifericos es:\n"
            for p in range (0, 6):
                print dicper(p) + dicestado(perifericos[p])
                


#Clase que lee el input sobre los procesos a realizar
class Lector:
    
    #Inicializa lector. Requiere la direccion del archivo con los procesos
    def __init__(self,direccion_archivo):
        self.direccion_archivo = direccion_archivo 
        self.contenido = None


    #Lee el contenido del archivo y lo guarda en el atributo contenido   
    def leer_archivo(self):
        try:
            f = open(self.direccion_archivo+".txt")
            self.contenido=f.read() 
            f.close()
        except IOError:
            print 'error'


    #Metodo que recibe un arreglo de strings y retorna la lista de procesos inicializados       
    def desglosar_contenido(self):
        arreglo_procesos = []
        procesos=self.contenido.split('\n')
        
        largo=len(procesos) - 1
        for i in range(0,largo):
            datos = procesos[i].split(';')
            if (datos[2]=='1' or datos[2]=='2'):
                arreglo_procesos.append(Llamada(procesos[i]))
            elif (datos[2]=='3' or datos[2]=='4'):
                arreglo_procesos.append(Mensaje(procesos[i]))
            elif (datos[2]=='5'):
                arreglo_procesos.append(Agregar_Contacto(procesos[i]))
            else:
                arreglo_procesos.append(Varios(procesos[i]))            
        arreglo_procesos = sorted(arreglo_procesos, key=lambda Proceso: Proceso.fecha) 
        return arreglo_procesos


#Clase que escribe en "memoria" los procesos que se van realizando    
class Memoria:

    #Inicializa memoria
    def __init__(self):
        self.rom='memoria.txt'
        self.contador=0 #Ve cuantas veces ha sido usado
        self.contacto='contacto.text'
        self.mensaje='mensaje.text'
        self.contador_contacto=0
        self.contador_sms=0
    #Escribe en memoria los procesos que se van ejecutando
    def escribir_memoria(self, proceso):
        #print proceso.nombre, proceso.fecha, proceso.tipo
        if self.contador>0:
            f=open(self.rom,'a')
            f.write(proceso.texto())
            f.write('\n')
            f.close()
        else:
            f=open(self.rom,'w')
            f.write(proceso.texto())
            f.write('\n')
            self.contador+=1
            f.close()
        if self.contador_contacto>0 and proceso.tipo==5:
            f=open(self.contacto,'a')
            f.write(proceso.nombre_contacto+"        ")
            f.write(str(proceso.numero_contacto))            
            f.write('\n')
            f.close()
        elif self.contador_contacto==0 and proceso.tipo==5:
            f=open(self.contacto,'w')
            f.write(proceso.nombre_contacto+"        ")
            f.write(str(proceso.numero_contacto))            
            f.write('\n')
            self.contador_contacto+=1
            f.close()
        elif self.contador_sms>0 and proceso.tipo==3:
            f=open(self.mensaje,'a')
            f.write(str(proceso.fecha)+"   Enviado   "+str(proceso.numero)+"   "+str(proceso.txt))
            f.write('\n')
            f.close()
        elif self.contador_sms==0 and proceso.tipo==3:
            f=open(self.mensaje,'w')
            f.write(str(proceso.fecha)+"   Enviado   "+str(proceso.numero)+"   "+str(proceso.txt))
            f.write('\n')
            self.contador_contacto+=1
            f.close()
        elif self.contador_sms>0 and proceso.tipo==4:
            f=open(self.mensaje,'a')
            f.write(str(proceso.fecha)+"   Recibido   "+str(proceso.numero)+"   "+str(proceso.txt))
            f.write('\n')
            f.close()
        elif self.contador_sms==0 and proceso.tipo==4:
            f=open(self.mensaje,'w')
            f.write(str(proceso.fecha)+"   Enviado   "+str(proceso.numero)+"   "+str(proceso.txt))
            f.write('\n')
            self.contador_contacto+=1
            f.close()

    
###########  MAIN DEL PROGRAMA  ###########

global memoria
global procesos
global ready
global running
global tiempo_ejecucion
global seguir
global top
global port

if len(sys.args) == 1:
    print "Debes correr el prgrama indicando el numero de puerto(python base.py 9999).\n Para correr una segunda instancia python base.py 9998 , etc\n NO SE PUEDE REPETIR"
    raw_input("apreta una tecla para terminar")
    sys.exit()
else:
    port = sys.argv[1]
    

## Seba y JP: receive connections estara esperando una conexion, recibira el mensaje y lo enviara a la funcion q lo 
## procesara
def process_received(proceso):
    #reemplazar pass con real codigo
    print "Se recibio: ", proceso

def receive_connections(): 
    while 1:
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(('127.0.0.1',port))
        s.listen(5)
        sock, addr = s.accept()
        print "conectado con ", addr
        new_process = sock.recv(1024)
        process_received(new_process) ##procesar proceso recibido
        s.close()


t = threading.Thread(target= receive_connections)
t.daemon = True
t.start()



def menu_sockets():
    s = socket(AF_INET, SOCK_STREAM)
    puerto = raw_input("Indique el puerto del otro celular")
    s.connect(('127.0.0.1', puerto))
    process_to_send = raw_input('Conectado!\nEnvia un proceso escribiendolo en el siguiente formato: formato;formato;formato')
    s.send(process_to_send)
    s.close()



tiempo_ejecucion = 0
entrada = raw_input('Ingrese nombre del archivo de input (sin extension)\n')
i = Lector(entrada)
i.leer_archivo()
seguir= True
top= False
memoria = Memoria()
procesos = i.desglosar_contenido()

ready = []
#con perifericos el running ses una lista, no un solo proceso
running = []


simu = Simulador()

p1 = Thread(target = simu.Simular)
p1.start()
  
cls()
print "Comandos:\n'salir'-> detiene programa\n'top'-> ver procesos (2 veces deja de ver los procesos)\n'nombre_proc;tipo;opc1;opc2sihay'-> ingresa un nuevo proceso\n'menu_sockets'-> menu para conectar con otro dispositivo"
while(seguir):

    orden = raw_input()
    if(orden == 'salir'):
        seguir = False
        #p1.terminate()
        break
    elif(orden == 'top'):
        if top:
            top = False
        else:
            top = True
    elif (orden == ""):
        pass
    elif (orden == "menu_sockets"):
        menu_sockets()    
    else:
        pu = orden.split(';')
        if(len(pu) <= 1):
            print "Comando incorrecto\n"
        elif (pu[2]=='1' or pu[2]=='2'):
            procesos.append(Llamada(orden))
        elif (pu[2]=='3' or pu[2]=='4'):
            procesos.append(Mensaje(orden))
        elif (pu[2]=='5'):
            procesos.append(Agregar_Contacto(orden))
        else:
            procesos.append(Varios(orden))
    orden = ""     
            
