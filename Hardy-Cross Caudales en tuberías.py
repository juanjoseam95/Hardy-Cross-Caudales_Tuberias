# -*- coding: utf-8 -*-
"""
Created on Tue Jun 07 23:56:04 2016

@author: juanjose
"""

import math as mt
import numpy as np
nodo=0
tuberias=0
i=0
j=0
relacionado=0
entrada=0
salida=0
cont=0
flujo=0
termino=0
Off=0
respuesta=0
ancho=0
alto=0
dx=0
dy=0
error=0 
respuesta=int(input("Si desea ingresar una geometria especifica escriba [1], de lo contrario escriba [0]: "))
while not(respuesta==0 or respuesta==1):
    print
    print "--->>>Debe ingresar [0] o [1]"
    respuesta=int(input("Si desea ingresar una geometria especifica escriba [1], de lo contrario escriba [0]: "))   
if respuesta==0:
    nodos=int(input("Ingrese el numero de nodos: "))
    while nodos<=0:
        print
        print "--->>>El numero de nodos debe ser mayor a cero"
        nodos=int(input("Ingrese el numero de nodos: "))      
    if nodos>0:
        if nodos%2==0:
            h=nodos/2
        else:
            h=(nodos+1)/2
        Tv=0
        Th=0
        for i in range(1,h):
            if i*i==nodos:
                Tv=i
                Th=i
        if Tv==0:
            burbuja=nodos   ####---->>> si son 4 nodos
            if burbuja<4:
                Th=2
                Tv=2
                burbuja=4
            else:
                if burbuja>4 and burbuja<=6:
                    Tv=3
                    Th=2
                    burbuja=6
                else:
                    if burbuja>6 and burbuja<9:
                        Th=2
                        Tv=4
                        burbuja=8
                    else:
                        if (burbuja%4==0):
                            contador=0
                            for i in range (burbuja):
                                if (burbuja%(i+1)==0):
                                    contador=contador+1 
                            x=0
                            V1=np.zeros((contador)) 
                            V2=np.zeros((contador))
                            Dif=np.zeros((contador))
                            j=0     
                            temporal=0     
                            for i in range (burbuja+1):
                                if (burbuja%(i+1)==0):
                                    x=(burbuja/(i+1))
                                    V1[j]=i+1
                                    V2[j]=x
                                    Dif[j]=(x-(i+1))
                                    j=j+1
                            for i in range ((contador/2)+1):
                                  for j in range ((contador/2)+1):
                                      x=Dif[i]
                                      if (Dif[j]<x):
                                          temporal=j                  
                            Tv=int(V1[temporal])
                            Th=int(V2[temporal])    
                        else:
                            i=1
                            iflag=1
                            while iflag==1:
                                iflag=1
                                burbuja=burbuja+1
                                if (burbuja%4==0):
                                    contador=0
                                    for i in range (burbuja):
                                        if (burbuja%(i+1)==0):
                                            contador=contador+1
                                    x=0
                                    V1=np.zeros((contador)) 
                                    V2=np.zeros((contador))
                                    Dif=np.zeros((contador))
                                    j=0
                                    temporal=0
                                    for i in range (burbuja+1):
                                        if (burbuja%(i+1)==0):
                                            x=(burbuja/(i+1))
                                            V1[j]=i+1
                                            V2[j]=x
                                            Dif[j]=(x-(i+1))
                                            j=j+1
                                    for i in range ((contador/2)+1):
                                        for j in range ((contador/2)+1):
                                            x=Dif[i]
                                            if (Dif[j]<x):
                                                temporal=j    
                                    Tv=int(V1[temporal])
                                    Th=int(V2[temporal])
                                    if Tv!=0:
                                        iflag=0
            Off=burbuja-nodos
            nodos=burbuja
else:
    if respuesta==1:
        nodos=int(input("Ingrese el numero de nodos: "))
        while nodos<=0:
            print
            print "--->>>El numero de nodos debe ser mayor a cero"
            nodos=int(input("Ingrese el numero de nodos: "))
        print
        ancho=float(input("Ingrese el ancho de la red (m): "))
        while ancho<=0:
            print
            print "--->>>El ancho de la red debe ser mayor a cero"
            ancho=float(input("Ingrese el ancho de la red (m): "))
        print
        alto=float(input("Ingrese la altura de la red (m): "))
        while alto<=0:
            print
            print "--->>>La altura de la red debe ser mayor a cero"
            alto=float(input("Ingrese la altura de la red (m): "))
        print
        dx=float(input("Ingrese la distancia horizontal entre nodos (m): "))
        while dx<=0:
            print
            print "--->>>La distancia horizontal entre nodos debe ser mayor a cero"
            dx=float(input("Ingrese la distancia horizontal entre nodos (m): "))
        print
        dy=float(input("Ingrese la distancia vertical entre nodos (m): "))
        while dy<=0:
            print
            print "--->>>La distancia vertical entre nodos debe ser mayor a cero"
            dy=float(input("Ingrese la distancia vertical entre nodos (m): "))
        if nodos>0 and ancho>0 and dx>0 and dy>0 and alto>0:
            Tv=int((ancho/dx)+1)
            Th=int((alto/dy)+1)
        else:
            error=1
            print "Todos los valores ingresados deben ser mayores que 0"
if error==0:
    print
    print "Numero de nodos=",nodos
    print "Tuberias horizontales=",Th
    print "Tuberias verticales=",Tv
    Grafo=np.zeros((nodos,nodos)) # grafo es si hay relacion entre nodos
    EntradaNodos=np.zeros((nodos))
    FlujosTuberias=np.zeros((nodos,nodos))
    Salidas=np.zeros((nodos)) 
    i=0
    """
    Aqui se enumera cada uno de los nodos de izquierda a derecha hasta llegar
    al ultimo de cada fila  en la siguiente fila se sigue enumerando
    """
    M=np.zeros((Th,Tv)) ## en m enumera los nodos
    contador=1
    for i in range(Th):
        for j in range(Tv):
            M[i,j]=contador
            contador=contador+1
    k=0
    c=0
    Cont=0
    i=0
    z=0
    """
    En este parte del codigo se hallan las relaciones que existen entre 
    nodos, es decir si cada nodo tiene un nodo adelante o atras de él
    """
    while z<nodos-1:
        for j in range(Tv):###<<<<<----------- aqui relacion entre derecha e izquierda
            if k<Tv-1:
                if (M[i,j]-M[c,k])==1:
                    Grafo[z,Cont]=1
                    Grafo[Cont,z]=1
                Cont=Cont+1
            else:
                j=Tv-1               
        i=i+1
        if Cont==nodos:
            k=k+1
            Cont=0
            i=0
            z=z+1
        else:
            if k>=Tv-1:
                k=0
                c=c+1
                Cont=0
                i=0
                z=z+1  
    k=0
    c=0
    Cont=0 
    i=0
    z=0
    """
    esta parte sirve para hallar las relaiones
    que hallan entre nodos superiores o inferiores
    """
    while z<nodos-1:
        for j in range(Tv):##<<<<<<-------- relacion arriba o abajo
            if c<Th-1:
                if (M[i,j]-M[c,k])==Tv:
                    Grafo[z,Cont]=1
                    Grafo[Cont,z]=1
                Cont=Cont+1
            else:
                j=Tv-1
        if i<Th-1:
            i=i+1
        else:
            if k<Tv-1:
                k=k+1
                i=0
                z=z+1
                Cont=0
            else:
                if c<Th-1:
                    c=c+1
                    k=0
                    i=0
                    z=z+1
                    Cont=0
                else:
                    z=nodos-1
    salida=float(input("Ingrese la cantidad que debe salir por cada nodo (Lt/s): "))
    while salida<=0:
        print
        print "--->>>La cantidad que debe salir por cada nodo debe ser mayor a cero"
        salida=float(input("Ingrese la cantidad que debe salir por cada nodo (Lt/s): ")) 
    EntradaNodos[0]=salida*(nodos-Off-1)
    print 
    print "Flujo que entra = ",EntradaNodos[0],"(Lt/s)"
    print
    i=1
    Salidas[0]=0
    while i<nodos:
        if nodos-i<=Off:
            Salidas[i]=0
        else:
            Salidas[i]=salida
        i=i+1
    """
    En esta parte del codigo se busca  dar una distribucion para el caso 0 
    en el cual se asume una distrbucion ideal en donde el fluido se divide
    en 2 cuando llega a un nodo
    """
    j=0
    while j<nodos:  ####----->>> distribucion del caso cero
        i=0
        Cont=0
        while i<nodos:
            if Grafo[j,i]==1:
                Cont=Cont+1
            i=i+1
        if Cont>0:
            if j==0:
                flujo=EntradaNodos[j]/Cont
            else:
                flujo=(EntradaNodos[j]-Salidas[j])/Cont
        i=0
        while i<nodos:
            if Grafo[j,i]==1:
                Grafo[i,j]=0
                EntradaNodos[i]=EntradaNodos[i]+flujo
                FlujosTuberias[j,i]=flujo
            i=i+1
        j=j+1        
    H=(Th-1)*(Tv-1)
    caudal=np.zeros((H*4))
    x=0
    Cont=0
    j=Tv
    Cont2=-1
    for i in range (H):  ###--->>> se guarda como se necesita abajo
        caudal[Cont]=FlujosTuberias[x,x+1]
        caudal[Cont+1]=FlujosTuberias[x+1,j+1]
        caudal[Cont+2]=FlujosTuberias[j,j+1]
        caudal[Cont+3]=FlujosTuberias[x,j]
        Cont2=Cont2+1
        if Cont2==Tv-2: ####--->>> aca asigna signos como son
            x=x+1
            j=j+1
            Cont2=-1
        x=x+1
        j=j+1
        Cont=Cont+4
    k=0
    for i in range((H*4)):
        x=0
        if k>1:
            if caudal[i]>0: 
                x=caudal[i]
                caudal[i]=(-1)*x
            else:
                x=caudal[i]
                caudal[i]=(-1)*x
        k=k+1
        if k>3:
            k=0
    Cont=0
    for i in range(H):
        print "Circuito ","(",i+1,")"," ""Q[",Cont,"]",round(caudal[Cont],5),"Q[",Cont+1,"]",round(caudal[Cont+1],5),"Q[",Cont+2,"]",round(caudal[Cont+2],5),"Q[",Cont+3,"]",round(caudal[Cont+3],5)
        Cont=Cont+4
        print
    NcircuitosH=Tv-1
    NcircuitosV=Th-1
    print "Numero de circuitos Horizontales =",NcircuitosH
    print "Numero de circuitos Verticales =",NcircuitosV
    print "Total de circuitos=",NcircuitosH*NcircuitosV
    print "Total caudales=",NcircuitosH*NcircuitosV*4
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"         Calculos de caudales                                                                       "
"                                                                                                            "   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Tolerancia=float(input("Ingrese su tolerancia (m): "))
while Tolerancia<=0:
    print
    print "--->>>La tolerancia debe ser mayor que cero"
    Tolerancia=float(input("Ingrese su tolerancia (m): "))
Rh=float(input("Ingrese la resistencia de tuberias horizontales: ")) 
while Rh<=0:
    print
    print "--->>>La resistencia de las tuberias horizontales debe ser mayor a cero"
    Rh=float(input("Ingrese la resistencia de tuberias horizontales: ")) 
Rv=float(input("Ingrese la resistencia de tuberias verticales: "))
while Rv<=0:
    print
    print "--->>>La resistencia de las tuberias verticales debe ser mayor a cero"
    Rv=float(input("Ingrese la resistencia de tuberias verticales: "))
x=int(input("""Si el diametro de todas las tuberias es igual escriba [1] 
Si verticales tienen un diametro y horizontales otro escriba [2]
Si las tuberias tienen diametros aleatoreos escriba [3]
""")) 
while not (x==1 or x==2 or x==3):
    print
    print "--->>>Debe escoger [1],[2] o [3] como su respuesta"
    x=int(input("""Si el diametro de todas las tuberias es igual escriba [1] 
Si verticales tienen un diametro y horizontales otro escriba [2]
Si las tuberias tienen diametros aleatoreos escriba [3]
    """)) 
Ncircuitos=NcircuitosH*NcircuitosV
Ncaudales=NcircuitosH*NcircuitosV*4
respuesta=int(input(" ¿Desea ver el procedimiento? [Si=1] [No=0]: "))
while not (respuesta==0 or respuesta==1):
    print
    print "--->>>Debe escoger [0] o [1] como su respuesta"
    respuesta=int(input(" ¿Desea ver el procedimiento? [Si=1] [No=0]: "))
ik=1
vueltas=0
if respuesta==1:
    print
    print "Procedimiento balanceo de caudales"    
while ik==1:
    rq=0
    j=1
    p=0
    g=0
    z=0
    for i in range (0,4):
        if i%2 !=0:
            rq= rq+abs(caudal[i])*Rv
        else:
            rq=rq+abs(caudal[i])*Rh
    hf=0
    for i in range(0,4):
            if i%2 !=0:
                    if caudal[i]<0:   
                        hf=hf-(caudal[i]**2*Rv)
                    else:
                        hf=hf+(caudal[i]**2*Rv)
            else:
                    if caudal[i]<0:   
                        hf=hf-(caudal[i]**2*Rh)
                    else:
                        hf=hf+caudal[i]**2*Rh
    dq=(-0.5*hf)/rq
    if abs(dq)>Tolerancia:
        vueltas=vueltas+1
        for i in range (0,4):
            caudal[i]=caudal[i]+dq
        if respuesta==1:
            print "----------------------------------"
            print("CIRCUITO 1")
            print "Sumatoria R*Q 1 =", rq
            print "Sumatoria Hf 1 =", hf
            print "Delta Q 1 =", dq
            for i in range (4):
                print "Q""(",i,")""=",caudal[i]
            print "--->>>Delta Q1 excede lo permitido"
            print 
    if abs (dq)<Tolerancia:
            ik=0 
#####################################################################Del segundo hasta el ultimo de cada fila
    if abs(dq)>Tolerancia:
            if NcircuitosH>1:
                    s=1
                    for c in range (NcircuitosV):
                            a=0
                            b=1
                            while b<NcircuitosH:
                                    g=g+4
                                    for y in range (NcircuitosH-1):                                            
                                            caudal[j+6]=-caudal[j]
                                            rq=0
                                            if s>=NcircuitosH:  
                                                    caudal[g]=-caudal[g-(NcircuitosH-1)*4-2]
                                            for i in range (g,g+4):
                                                    if i%2 !=0:
                                                            rq=rq+abs(caudal[i])*Rv
                                                    else:
                                                           
                                                            rq=rq+abs(caudal[i])*Rh
                                            hf=0
                                            for i in range (g,g+4):
                                                    if i%2 !=0:
                                                            if caudal[i]<0:   
                                                                    hf=hf-(caudal[i]**2*Rv) 
                                                            else:
                                                                    hf=hf+caudal[i]**2*Rv         
                                                    else:
                                                            if caudal[i]<0:
                                                                    hf=hf-(caudal[i]**2*Rh)
                                                            else:
                                                                    hf=hf+caudal[i]**2*Rh
                                            dq=(-hf*0.5)/rq        
                                            for i in range (g,g+4):
                                                    caudal[i]=caudal[i]+dq
                                            if respuesta==1:
                                                print "CIRCUITO",(z+2)
                                                print "Sumatoria R*Q" ,(z+2), "=", rq
                                                print "Sumatoria Hf" ,(z+2), "=", hf
                                                print "Delta Q" ,(z+2), "=", dq        
                                                for i in range (g,g+4):
                                                    print "Q" "(" ,i, ")" "=", caudal[i]
                                                print
                                            caudal[j]=-caudal[j+6]
                                            if s>=NcircuitosH:   
                                                    caudal[g-(NcircuitosH-1)*4-2]=-caudal[g] 
                                            j=j+4
                                            b=b+1
                                            z=z+1
                                            s=s+1
                                            if g<Ncaudales-4:
                                                    if NcircuitosV>1:
                                                            if g>NcircuitosH*4-1:
                                                                    caudal[g]=-caudal[g-(NcircuitosH-1)*4-2] 
                                            g=g+4                                           
              ##################################################los primero de cada fila                                        
                            if NcircuitosV>1:
                                    if s<Ncircuitos:
                                            while a<NcircuitosV-1:    #<-
                                                    if g>NcircuitosH*4-1:
                                                            caudal[g]=-caudal[g-(NcircuitosH-1)*4-2]
                                                    rq=0
                                                    for i in range (g,g+4):
                                                            if i%2 !=0:
                                                                    rq= rq+abs(caudal[i])*Rv
                                                            else:
                                                                    rq=rq+abs(caudal[i])*Rh
                                                    hf=0
                                                    for i in range(g,g+4):
                                                            if i%2 !=0:
                                                                    if caudal[i]<0:
                                                                            hf=hf-(caudal[i]**2*Rv)
                                                                    else:
                                                                            hf=hf+(caudal[i]**2*Rv)
                            
                                                            else:
                                                                    if caudal[i]<0:   
                                                                            hf=hf-(caudal[i]**2*Rh)
                                                                    else:
                                                                            hf=hf+caudal[i]**2*Rh
                                                    dq=(-0.5*hf)/rq
                                                    j=g+1
                                                    a=a+NcircuitosV-1                                                    
                                                    for i in range (g,g+4):
                                                            caudal[i]=caudal[i]+dq                                         
                                                    caudal[g-(NcircuitosH-1)*4-2]=-caudal[g]
                                                    if respuesta==1:
                                                        print "CIRCUITO",z+2
                                                        print "Sumatoria R*Q" ,(z+2), "=", rq
                                                        print "Sumatoria Hf" ,(z+2), "=", hf
                                                        print "Delta Q" ,(z+2), "=", dq
                                                        for i in range (g,g+4):
                                                            print "Q" "(" ,i, ")" "=", caudal[i]
                                                        print
                                                    z=z+1
                                                    s=s+1                                                  
   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Solo verrticales                               
            if NcircuitosH==1 and NcircuitosV>1:
                    for c in range (NcircuitosV-1):
                            g=g+4
                            rq=0 
                            caudal[g]=-caudal[g-2]
                            for i in range (g,g+4):
                                    if i%2 !=0:
                                            rq=rq+abs(caudal[i])*Rv
                                    else:
                                            rq=rq+abs(caudal[i])*Rh
                            hf=0
                            for i in range(g,g+4):
                                    if i%2 !=0:
                                            if caudal[i]<0:   
                                                hf=hf-(caudal[i]**2*Rv)
                                            else:
                                                hf=hf+(caudal[i]**2*Rv)                            
                                    else:
                                            if caudal[i]<0:   
                                                hf=hf-(caudal[i]**2*Rh)
                                            else:
                                                hf=hf+caudal[i]**2*Rh
                            dq=(-0.5*hf)/rq
                            for i in range (g,g+4):
                                     caudal[i]=caudal[i]+dq
                            if respuesta==1:
                                print "CIRCUITO",(z+2)
                                print "Sumatoria R*Q" ,(z+2), "=", rq
                                print "Sumatoria Hf" ,(z+2), "=", hf
                                print "Delta Q" ,(z+2), "=", dq
                                for i in range (g,g+4):
                                    print "Q""(",i,")""=",caudal[i]
                                print
                            caudal[g-2]=-caudal[g]
                            z=z+1                           
if respuesta==1:                                
        print "Delta Q1=",dq,", tolerancia cumplida."
        print
################################ velocidad
vel=np.zeros((Ncaudales))
if x==1:
    d=float(input("Ingrese el diametro de las tuberias (m): "))
    while d<=0:
        print
        print "--->>>El diametro de las tuberias debe ser mayor a cero"
        d=float(input("Ingrese el diametro de las tuberias (m): "))
    print
    if d>0:
        if respuesta==1:
            print "Procedimiento velocidad"
            print
        for i in range (Ncaudales):
            vel[i]=(4*abs(caudal[i]*0.001))/(mt.pi*d**2)
            if respuesta==1:
                print "Velocidad Q[",i,"]=","(4*",abs(caudal[i]),")/(3.1416*",d,"**2)"
                print "Velocidad Q[",i,"]=",vel[i]
                print
if x==2:
    d=float(input("Ingrese el diametro de las tuberias horizontales (m): "))
    while d<=0:
        print
        print "--->>>El diametro de las tuberias horizontales debe ser mayor a cero"
        d=float(input("Ingrese el diametro de las tuberias horizontales (m): "))
    d2=float(input("Ingrese el diametro de las tuberias verticales (m): "))
    while d2<=0:
        print
        print "--->>>El diametro de las tuberias verticales debe ser mayor a cero"
        d2=float(input("Ingrese el diametro de las tuberias verticales (m): "))
    print
    if d>0 and d2>0:
        if respuesta==1:
            print "Procedimiento velocidad"
            print
        for i in range (Ncaudales):
            if i%2 !=0:
                vel[i]=(4*abs(caudal[i]*0.001))/(mt.pi*d2**2)
            else:
                 vel[i]=(4*abs(caudal[i]*0.001))/(mt.pi*d**2)
            if respuesta==1:
                print "Velocidad Q[",i,"]=","(4*",abs(caudal[i]),")/(3.1416*",d,"**2)"
                print "Velocidad Q[",i,"]=",vel[i]
                print
if x==3:
    d=np.zeros((Ncaudales))
    for i in range ((Ncaudales)):
        if x!=0:
            print
            print "Tuberia",i
            d[i]=float(input("Ingrese el diametro de la tuberia (m): "))
            while d[i]<=0:
                print
                print "El diametro de la tuberia","[",i,"]","debe ser mayor a cero"
                d[i]=float(input("Ingrese el diametro de la tuberia (m): "))
            print
            
    if x!=0:
        if respuesta==1:
            print "Procedimiento velocidad"
            print
        for i in range (Ncaudales):
            vel[i]=(4*abs(caudal[i]*0.001))/(mt.pi*d[i]**2)
            if respuesta==1:
                print "Velocidad Q[",i,"]=","(4*0.001*",abs(caudal[i]),")/(3.1416*",d[i],"**2)"
                print "Velocidad Q[",i,"]=",vel[i]
                print
######################## respuestas
    
if respuesta==0:                                
    print "Delta Q1=",dq,", tolerancia cumplida."
    print
Cont=0
print
print "RESULTADOS"
for x in range (0,Ncircuitos):
        print "Circuito", "(",x+1,")"," ","Q","[",Cont,"]",round (caudal[Cont],5),"Q","[",Cont+1,"]",round (caudal[Cont+1],5),"Q","[",Cont+2,"]",round (caudal[Cont+2],5),"Q","[",Cont+3,"]",round (caudal[Cont+3],5)
        Cont=Cont+4
        print
print "Caudales (Lt/s)""         ","Velocidades (m/s)"
for x in range (Ncaudales):
        print "Q" "(",(x),")" "=", round (caudal[x],5),"             ",round(vel[x],6)
        print
print
print "Vueltas =",vueltas

   




#la j controla las tuberias que se comparten verticales
#la y las veces que se va a repetir el codigo segun los circuitos que hallan horizontales
# hacer que no calcule el primer circuito cuando dq cumpla
#las g me controlan el cambio de circuito para que empiece a calcular desde la barra de arrba
#p controla el numero del tubo que va abajo
#la z controla el numero que le imprime al caudal
# s cuenta para que cuando llegue al ultimo circuito no entre mas en el que calcula los primeros de cada fila
# la a es para que si son solo circuitos horizontales no entre al que hace el primero de cada fila
###----->>>> nota: poner cual es la separacion entre tuverias horizontal y verticalmente si el programa arma eso
