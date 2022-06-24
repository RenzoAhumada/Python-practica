
import json
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

'''class  alumnos:
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

def buscaropcion():
   def carga():
    try:
        _matricula = int(input("Ingrese la matricula del alumno: "))
        _nombre = input("Ingrese el nombre del alumno: ")
        _apellido = input("Ingrese el apellido del alumno: ")
    except:
        print("Hubo una falla al cargar los datos.")

    _alumno = {'matricula': _matricula, "datos": {'nombre': _nombre, 'apellido': _apellido}}
    alumno.setAlumno(_alumno)'''


def writeTOJSONFile(path, filematricula, data):
    json.dump(data, path)

path= './'

def cargar():
    a = caja_matricula.get()
    b = caja_nombre.get()
    c = caja_apellido.get()
    print(a)
    print(b) 
    print(c)   
    data={}
    data['Matricula'] = a
    data['Nombre'] = b
    data['Apellido'] = c
    files = [('JSON File', '*.json')]
    filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='Alumnos')
    (filepos, fileMatricula, data)
    writeToJSONFile(filepos, fileMatricula, data)




ventana = tk.Tk()
ventana.config(width=600, height=400)

etiqueta_matricula = ttk.Label(text="Ingrese numero de matricula del alumno: ")
etiqueta_matricula.place(x=20, y=20)
etiqueta_nombre = ttk.Label(text="Ingrese nombre del alumno: ")
etiqueta_nombre.place(x=20, y=40)
etiqueta_apellido = ttk.Label(text="Ingrese apellido del alumno: ")
etiqueta_apellido.place(x=20, y=60)

caja_matricula = ttk.Entry()
caja_matricula.place(x=250, y=20, width=80)
caja_nombre = ttk.Entry()
caja_nombre.place(x=250, y=40, width=80)
caja_apellido = ttk.Entry()
caja_apellido.place(x=250, y=60, width=80)

boton_enviar_opcion = ttk.Button(text="Agregar alumno", command= cargar)
boton_enviar_opcion.place(x=20, y=80)
etiqueta_alumnos = ttk.Label(text="Los alumnos son: ")
etiqueta_alumnos.place(x=20, y= 200)

ventana.mainloop()







'''while opcion !=4:
    print("Ingrese en la opcion 0 seguir cargando alumno, 1 Terminar y guardar, 2 Terminar y cancelar, 3 Ver los alumnos")

    opcion = int(input("Ingrese la opcion: "))
    if opcion == 0: MA.carga()
    if opcion == 1: MA.alumno.saveInFile()
    if opcion == 2: opcion = 1
    if opcion == 3: MA.alumno.showData()
    if opcion == 4:
        break'''


