
from importlib.metadata import entry_points
import json
from sqlite3 import Row
from tabnanny import check
from tkinter import *
import json
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
window = Tk()
window.geometry('640x300')
window.title('Alumnos')

matricula = Label(window, text='Matricula: ')
Matricula = Entry(window)
nombre = Label(window, text='Nombre')
Nombre = Entry(window)
apellido = Label(window, text='Apellido')
Apellido = Entry(window)
submit = Button(window, text='Enviar', command = check).grid(row=3, column=1)

test = 1
def writeToJSONFile(path, fileName, data):
        json.dump(data, path)

path= './'

def check():
    a = Matricula.get()
    b = Nombre.get()
    c = Apellido.get()
    print(a)
    print(b) 
    print(c)   
    data={}
    data['Matricula'] = a
    data['Nombre'] = b
    data['Apellido'] = c
    files = [('JSON File', '*.json')]
    fileName = 'Alumnos'
    filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='Alumnos')
    writeToJSONFile(filepos, fileName, data)



matricula.grid(row=0, column=0)
nombre.grid(row=1, column=0)
apellido.grid(row=2, column=0)
Matricula.grid(row=0, column=1)
Nombre.grid(row=1, column=1)
Apellido.grid(row=2, column=1)


mainloop()







'''while opcion !=4:
    print("Ingrese en la opcion 0 seguir cargando alumno, 1 Terminar y guardar, 2 Terminar y cancelar, 3 Ver los alumnos")

    opcion = int(input("Ingrese la opcion: "))
    if opcion == 0: MA.carga()
    if opcion == 1: MA.alumno.saveInFile()
    if opcion == 2: opcion = 1
    if opcion == 3: MA.alumno.showData()
    if opcion == 4:
        break'''


