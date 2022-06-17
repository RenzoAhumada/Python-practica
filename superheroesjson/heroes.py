
#Importamos json
import json

#Creamos una nueva lista vacia para poder appendiar los datos
heroes = {}
#Le damos la llave hereos a la lista de hereos para poder appendiar los difrentes tipos de hereos
heroes["hereos"] = []
#Se appendean los datos
heroes["hereos"].append({"nombre": "Flash",
                        "identidadSecreta": "Bartholomew Henry 'Barry' Allen",
                        "poderes": [
                        "Inmensa velocidad",
                        "agilidad",
                        "Electrokinesis"]
                        })

heroes["hereos"].append({"nombre": "Batman",
                        "identidadSecreta": "Bruce Wayne",
                        "poderes": ["Super fuerza",
                        "super velocidad"]})

heroes["hereos"].append({ "nombre": "Super Man",
                        "identidadSecreta": "Clark Joseph Kent",
                        "poderes": ["Super fuerza",
                        "super velocidad",
                        "resistencia", 
                        "agilidad",
                        "reflejos",
                        "durabilidad", 
                        "sentidos y longevidad"
                        ]})
#Imprimimos por pantalla la lista que tiene el json guardad.
print(heroes)
