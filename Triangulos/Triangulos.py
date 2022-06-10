
#Importamos la clase Triangulo para poder llamarla y poder utilizar su logica
import ClassTriangulo as CT
#Una vez creado el triangulo creamos un bucle while, el cual se repetira hasta que el usuario coloque el numero correspondiente para salir
triangulo1 = CT.triangulo(lado1=None,lado2=None,lado3=None)
opcion=0
while opcion != 4:

    #Se muestra el pequeño menu para poder elegir algunas de las opciones teniendo como 1 2 3  y 4 para salir, hasta que el usuario no coloque el numero 4 no podra salir
    print("Para mostrar los lados del triangulo seleccione 1, para ver lado mayor seleccione 2, para ver tipo de triangulo seleccione 3, para salir seleccione 4")
    opcion=int(input("Seleccione su opcion "))
    if opcion == 1:
        #Se mostraran los lados los cuales han sido pasados por parametros
        triangulo1.mostrarLados()
    elif opcion == 2:
        #Se mostrara el lado mayor pasados por parametros
        triangulo1.ladoMayor()
    elif opcion == 3:
        #Se mostrara el tipo de triangulo segun los parametros
        triangulo1.mostrarTipo()
    elif opcion > 4:
        print("Opcion no encontrada =(")    
    else:
        pass


