import MainAlumnos as MA
opcion=0
while opcion !=1:
    print("Ingrese en la opcion 0 seguir cargando alumno, 1 Terminar y guardar, 2 Terminar y cancelar, 3 Ver los alumnos")

    opcion = int(input("Ingrese la opcion: "))
    if opcion == 0: MA.carga()
    if opcion == 1: MA.alumno.saveInFile()
    if opcion == 2: opcion = 1
    if opcion == 3: MA.alumno.showData()
