'''
Desarrollado por Javier "JaviHax" Rivas 2019.
'''

import matplotlib.pyplot as plt #import del plotter
import time as tm             #import del time control
from os import system as sys    #import dela libreria de sistema

def inicio():
    print("\033[1;32;40m ")
    print("██╗     ██╗███╗   ██╗      ██████╗ ██████╗  ██████╗")
    print("██║     ██║████╗  ██║      ██╔══██╗╚════██╗██╔════╝")
    print("██║     ██║██╔██╗ ██║█████╗██████╔╝ █████╔╝██║  ███╗")
    print("██║     ██║██║╚██╗██║╚════╝██╔══██╗ ╚═══██╗██║   ██║")
    print("███████╗██║██║ ╚████║      ██║  ██║██████╔╝╚██████╔╝")
    print("╚══════╝╚═╝╚═╝  ╚═══╝      ╚═╝  ╚═╝╚═════╝  ╚═════╝ v1.0")
    print("\t\t\t\t\tBy JaviHax.")
    print("El siguiente programa resolvera un problema de regresion polinomial.")
    tm.sleep(2)#sleep para controlar la muestra.
    sys("clear")
    data_crunch()
    
def data_crunch():#este bloque toma los datos para nuestros puntos de graficado
    arrayx = []
    arrayy = []
    while True:#bloque de captura de errores
        try:
            n = int(input("Ingrese el numero de iteraciones: "))
            break
        except ValueError:
            print("Dato no valido.")
    
    print("A continuacion se procedera a rellenar los valores dentro del array X")
    tm.sleep(2)
    sys("clear")
    
    for i in range(n):#rellenado de la columna x
        while True:#bloque de captura de errores
            try:
                b = float(input(f"Ingrese el valor {i+1} de su array X: "))
                break
            except ValueError:
                print("Dato no valido, intente nuevamente.")
                tm.sleep(1)
                sys("clear")
        arrayx.append(b)
    
    print("A continuacion se procedera a rellenar los valores dentro del array Y")
    tm.sleep(2)
    sys("clear")

    for i in range(n):#rellenado de la columna y
        while True:#bloque de captura de errores
            try:
                b = float(input(f"Ingrese el valor {i+1} de su array Y: "))
                break
            except ValueError:
                print("Dato no valido, intente nuevamente.")
                tm.sleep(1)
                sys("clear")
        arrayy.append(b)

    print("Los datos tabulados son:")
    print(f"los datos de X son: {arrayx}")
    print(f"los datos de Y son: {arrayy}")
    print("A continuacion se mostraran los datos de forma grafica.")
    tm.sleep(2)
    sys("clear")
    plotter1(arrayx, arrayy)#graficado de puntos dados por el problema
    '''
    NOTA IMPORTANTE:
    a continuacion generaremos calculos los cuales requieren de la suma completa
    de todos los valores contenidos en un array, para esto es importante el desarrollo
    de un listado como glosario, este se desarrollara mas adelante.
    '''
    x2 = []
    x3 = []
    x4 = []
    xy = []
    x2y = []
    for i in arrayx:#valor de x^2
        x2.append(i**2)
    for i in arrayx:#valor de x^3
        x3.append(i**3)
    for i in arrayx:#valor de x^4
        x4.append(i**4)
    for i in range(n):
        xy.append(arrayx[i]*arrayy[i])
    for i in range(n):
        x2y.append((arrayx[i]**2)*arrayy[i])
    
    x2 = sum(x2)#valor de sumatoria x^2
    x3 = sum(x3)#valor de sumatoria x^3
    x4 = sum(x4)#valor de sumatoria x^4
    xy = sum(xy)#valor de sumatoria de xy
    x2y = sum(x2y)#valor de sumatoria x2y
    sumx = sum(arrayx)#sumatoria de x
    sumy = sum(arrayy)#sumatoria de y
    '''
    GLOSARIO:
    -x2 significa x al cuadrado
    -x3 significa x al cubo
    -x4 significa x ala cuarta
    -xy significa x por y
    -x2y significa x al cuadrado por y
    -sumx significa la sumatoria de x
    -sumy significa la sumatoria de y
    '''
    print(f"El valor de X^2 es: {x2}")
    print(f"El valor de X^3 es: {x3}")
    print(f"El valor de X^4 es: {x4}")
    print(f"El valor de X*Y es: {xy}")
    print(f"El valor de X^2*Y es: {x2y}")
    print(f"El valor dela sumatoria de X es: {sumx}")
    print(f"El valor dela sumatoria de Y es: {sumy}")

    f1 = [n, sumx, x2, sumy]
    f2 = [sumx, x2, x3, xy]
    f3 = [x2, x3, x4, x2y]

    raices = Gauss_Jordan(f1, f2, f3)
    print("SE HA RESUELTO EL POLINOMIO, SU RESULTADO SERIA EL SIGUIENTE:")
    print(f"{raices[0]}X^2 + {raices[1]}X + {raices[2]}")
    fx = []
    for i in arrayx:
        fx.append(((raices[0]*(i**2)) + (raices[1]*i) + raices[2]))
    
    plotter2(arrayx, arrayy, fx)
    sys("clear")
    print("GRACIAS POR USAR LA HERRAMIENTA!!!.")
    tm.sleep(3)

    b = int(input("Desea regresar al inicio. 1- si. 2- no: "))
    if b == 1:
        sys("clear")
        print("Regresando al inicio...")
        tm.sleep(3)
        inicio()
    else:
        sys("clear")
        print("Gracias por usar nuestro programa...")
   
def Gauss_Jordan(fila_uno, fila_dos, fila_tres):

    L = fila_uno[0]#u stands for upder in the division
    for i in range(len(fila_uno)):
        U = fila_uno.pop(0)
        insert = U/L#here happens the division
        fila_uno.append(insert)#replacing with the new values

    b = fila_dos[0]
    if b > 0:#This makes the first validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_dos.pop(0)
            b = aux + auxiliary_array[i]
            fila_dos.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_dos.pop(0)
            b = aux - auxiliary_array[i]
            fila_dos.append(b)

    b = fila_dos[1]
    for i in range(len(fila_dos)):
        fila_dos.append(fila_dos.pop(0)/b)

    b = fila_tres[0]
    if b > 0:#This makes the second validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_tres)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_uno:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_uno)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux - auxiliary_array[i]
            fila_tres.append(b)

    b = fila_tres[1]
    if b > 0:#This makes the second validation process in our program
        b *= -1
        auxiliary_array = []
        for i in fila_dos:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_dos)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    else:#this part also makes a validation but in the oposite case of the upper method
        b = abs(b)
        auxiliary_array = []
        for i in fila_dos:#this part fills a new array with new info
            aux = i * b
            auxiliary_array.append(aux)
        
        for i in range(len(fila_dos)):#this makes the calculus between the 2 rows
            aux = fila_tres.pop(0)
            b = aux + auxiliary_array[i]
            fila_tres.append(b)

    b = fila_tres[2]
    for i in range(len(fila_tres)):
        fila_tres.append(fila_tres.pop(0)/b)
    
    b = fila_dos[2]
    if b > 0:
        b *= -1
        for i in fila_tres[2:]:
            aux = i * b
            c = fila_dos.pop(2)
            fila_dos.append(aux + c)

    else:
        b = abs(b)
        for i in fila_tres[2:]:
            aux = i * b
            c = fila_dos.pop(2)
            fila_dos.append(aux + c)

    b = fila_uno[2]
    if b > 0:
        b *= -1
        auxiliary_array = []
        for i in fila_tres:
            aux = i * b
            auxiliary_array.append(aux)

        for i in range(len(fila_uno[1:])):
            aux = fila_uno.pop(1)
            b = aux + auxiliary_array[i+1]
            fila_uno.append(b)

    else:
        b = abs(b)
        auxiliary_array = []
        for i in fila_uno:
            aux = i * b
            auxiliary_array.append(aux)

        for i in range(len(fila_uno)):
            aux = fila_uno.pop(1)
            b = aux + auxiliary_array[i]
            fila_uno.append(b)

    b = fila_uno[1]
    if b > 0:
        b *= -1
        aux = fila_uno.pop(1)
        c = aux + b
        fila_uno.insert(1, c)
        aux = fila_uno.pop(3)
        c = b * fila_dos[3]
        b = aux + c
        fila_uno.insert(3, b)
    else:
        b = abs(b)
        aux = fila_uno.pop(1)
        c = aux + b
        fila_uno.insert(1, c)
        aux = fila_uno.pop(3)
        c = b * fila_dos[3]
        b = aux + c
        fila_uno.insert(3, b)

    X = fila_uno[3]
    Y = fila_dos[3]
    Z = fila_tres[3]

    print(f"Los valores encontrados por el metodo de Gauss-Jordan son:\nX = {round(X, 2)}\nY = {round(Y, 2)}\nZ = {round(Z, 2)}")
    raices = [X, Y, Z]
    tm.sleep(3)
    sys("clear")
    return raices

def plotter2(x, y, fx):
    plt.plot(x,fx, color = 'blue')
    plt.plot(x, y, 'ro', color = 'red',)
    plt.plot([0,0],[-100,100], color = 'black')
    plt.plot([-100,100],[0,0], color = 'black')
    plt.title("Estado Polinomial Completo.")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.axis([-1,6,-1,63])
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.show()

def plotter1(x, y):
    plt.plot(x, y, 'ro', color = 'red',)
    plt.plot([0,0],[-100,100], color = 'black')
    plt.plot([-100,100],[0,0], color = 'black')
    plt.title("Puntos dados por la tabla")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.axis([-1,6,-1,63])
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.show()

inicio()