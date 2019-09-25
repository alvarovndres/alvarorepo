#COMENTARIOS
'''Una calculadora para
aprender Python'''
from os import system

def Pausa():
    print("Presione una tecla para continuar")
    
system("cls")

def Sumar(a,b):
    print("La suma es :",str(a+b))
    
def Restar(x,y):
    resta=x-y
    print(f"La resta es {resta}")
    
def Multiplicar(q,w):
    multi=q*w
    print(f"La multiplicacion es {multi}")

def Dividir(e,r):
    divi=e/r
    print(f"La division es {divi}")

def Menu():
    print("""SELECCIONE ALGUNA OPERACION
    1.Sumar
    2.Restar
    3.Multiplicar
    4.Dividir
    9.Salir""")
    
    
while True:
        
        Menu()
        
        op=int(input("Ingrese su opcion: "))
        
        if(op!=9 and op>=1 and op<=4):
            num1=float(input("Ingrese un numero: "))
            num2=float(input("Ingrese otro numero: "))
            
        if op==1:
            Sumar(num1,num2)
        elif op==2:
            Restar(num1,num2)
        elif op==3:
            Multiplicar(num1,num2)
        elif op==4:
            Dividir(num1,num2)
        elif op==9:
            print("Fin del Programa.....")
            Pausa()
            break
        else:
            print("Opcion no valida....")
        Pausa()