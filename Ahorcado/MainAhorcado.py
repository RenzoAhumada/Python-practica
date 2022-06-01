import ModoFacilAhorcado


print("Elija una dificultad siendo 1 facil, 2 medio y dificil")
#Desde aqui se llama el menu para poder interactuar con la dificultad para cantidad de intentos
#Dependiendo la opcion es la funcion a la que se llama y abrira otro bucle

while True:
    opcion = int(input("Elija dificultad: "))
    if opcion==1:
        ModoFacilAhorcado()
    elif opcion==2:
        pass
    elif opcion==3:
        pass
    else:
        print("Ups esa opcion no es correcta")


