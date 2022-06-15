import json


heroes = {}

heroes["hereos"] = []

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

print(heroes)
