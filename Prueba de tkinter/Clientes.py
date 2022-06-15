import json

class cliente():
    numeroCliente = {}

    def loadJason(self):
        with open('clientes.json') as json_file:
            self.numeroCliente = json.load(json_file)
            print(self.numeroCliente)

    def setCliente(self,_Cliente):
        self.numeroCliente[_cliente['numeroCliente']]=_cliente['datos']
        print(self.numeroCliente)   

    def saveInFile(self):
        jsonFile = open("clientes.json", 'w')
        jsonFile.write(json.dumps(self.numeroCliente,
                        skipkeys= True,
                        allow_nan= True,
                        indent=4, ensure_ascii=False))
        jsonFile.close 

    def showData(self):
        print(self.numeroCliente)  


clientes = cliente()
cliente.loadJason
      