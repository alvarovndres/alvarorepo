#COMENTARIOS
'''Una calculadora para
aprender Python'''
from os import system

def Pausa():
    print("Presione una tecla para continuar")
system("cls")
def Sumar():
    pass

def Restar():
    pass

def Multiplicar():
    pass

def Dividir():
    pass

def Menu():
    print("""1.Sumar
    2.Restar
    3.Multiplicar
    4.Dividir
    9.Salir""")
    
    
    while True:
        num1=float(input("Ingrese un numero"))
        num1=float(input("Ingrese otro numero"))
        Menu()
        op=int(input("Ingrese su opcion: "))
        if op==1:
            Sumar(num1,num2)
        elif op==2:
            Restar()
        elif op==3:
            Multiplicar()
        elif op==4:
            Dividir()
        elif op==9:
            print()"Fin del Programa)
            Pausa()
            break
        else:
            print("Opcion no valida")
        Pausa()