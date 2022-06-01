
import Logica

print("Bienvenido a esta pequeña calculadora")
#Se definen los numeros para poder enviarlos como parametros
num1 = float(input("Introduzca el valor 1"))
num2 = float(input("Introduzca el valor 2"))

opcion=0

#Bucle para poder elegir una opcion
while True:
    print("Elija que le gustaria hacer:")
    print("Opcion 1 suma")
    print("opcion 2 resta")
    print("Opcion 3 divicion")
    print("Opcion 4 multiplicar")
    print("Opcion 5 apagar calculadora")
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(Logica.sumar(num1,num2))
    elif opcion == 2:
        print(Logica.resta(num1,num2))
    elif opcion == 3:
        print(Logica.divicion(num1,num2))
    elif opcion == 4:
        print(Logica.multiplicacion(num1,num2))
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")




