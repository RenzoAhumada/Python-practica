import json
import tkinter as tk
from tkinter import *
class alumnos:
    matriculas = {}

    def loadJason(self):
        with open('Alumnos.json') as jason_file:
            self.matriculas = json.load(jason_file)
            print(self.matriculas)

    def setAlumno(self,_alumno):
        self.matriculas[_alumno['matricula']]=_alumno['datos']
        print(self.matriculas)

    def saveInFile(self):
        jsonFile = open("alumnos.json", 'w')
        jsonFile.write(json.dumps(self.matriculas,
                        skipkeys= True,
                        allow_nan= True,
                        indent=4, ensure_ascii=False))
        jsonFile.close

    def showData(self):
        print(self.matriculas)

alumno = alumnos()
alumno.loadJason
opcion=0
def carga():
    try:
        _matricula = int(input("Ingrese la matricula del alumno: "))
        _nombre = input("Ingrese el nombre del alumno: ")
        _apellido = input("Ingrese el apellido del alumno: ")
    except:
        print("Hubo una falla al cargar los datos.")

    _alumno = {'matricula': _matricula, "datos": {'nombre': _nombre, 'apellido': _apellido}}
    alumno.setAlumno(_alumno)

while opcion !=1:
    print("Ingrese en la opcion 0 seguir cargando alumno, 1 Terminar y guardar, 2 Terminar y cancelar, 3 Ver los alumnos")

    opcion = int(input("Ingrese la opcion: "))
    if opcion == 0: carga()
    if opcion == 1: alumno.saveInFile()
    if opcion == 2: opcion =1
    if opcion == 3: alumno.showData()




