import os
from os import system

from Personaje import Personaje
import random
nombresEnemigos = ["Wige",
                   "Haethug",
                   "Giles",
                   "Ardwund",
                   "Tephye Aryn",
                   "Thelry",
                   "Wulfa",
                   "Sige",
                   "Elrer",
                   "Aerid"]
clasesEnemigos = {"Magicos": ["Brujo", "Hechicero", "Mago"],
                  "Fisicos": ["Guerrero", "Monje", "Barbaro"],
                  "Curanderos": ["Druida", "Clerigo Oscuro"],
                  "Arqueros": ["Batidor", "Explorador"]
                  }
razasEnemigos = ["Goblin",
                 "Orco",
                 "Semiorco",
                 "Kobold",
                 ]
tecnicas = {"Magicos": ["Bola de fuego", "Rayo", "LLamarada"],
                  "Fisicos": ["Espada", "Puñetazo", "Porrazo"],
                  "Curanderos": ["Gracia Divina", "Inflinjir Heridas"],
                  "Arqueros": ["Abocajarro", "Disparo Rapido", "Disparo Penetrante"]
                  }
tipos = []
for tipo in clasesEnemigos.keys():
    tipos.append(tipo)
tipoMousntro = random.choice(tipos)
clase = random.choice(clasesEnemigos[tipoMousntro])

tiposTecnica = []
for tipo in tecnicas.keys():
    tiposTecnica.append(tipo)
tipoTecMonster = random.choice(tiposTecnica)
tecnicaMonster = random.choice(tecnicas[tipoTecMonster])

#Randoms Personaje
randomVidaPersonaje = random.choice(range(10, 15))
randomEscudoPersonaje = random.choice(range(10, 15))
randomIniciativaPersonaje = random.choice(range(1, 5))

#Randoms Monster
nombreMousntro = random.choice(nombresEnemigos)
razaMousntro = random.choice(razasEnemigos)
clase = random.choice(clasesEnemigos[tipoMousntro])
randomVidaMousntro = random.choice(range(10, 20))
randomEscudoMousntro = random.choice(range(10, 15))
randomIniciativaMonster = random.choice(range(1, 5))

m = Personaje(nombreMousntro, razaMousntro, clase, "","","",randomIniciativaMonster,"")
m.setVida(m.VidaPersonaje(randomVidaMousntro, tipoMousntro))
m.setEscudo(m.EscudoPersonaje(randomEscudoMousntro, tipoMousntro))
m.setAtaque(m.AtaqueBase(tipoMousntro))
m.setTecnicas(tecnicas.get(tipoMousntro))
bucle = True
tipoPersonaje = ""
p1 = Personaje("", "", "", "", "", "", "", "")
p1.nombre = input("Nombre de personaje: ")

print(""" -- ELIGE TU CLASE --
    [1] Guerrero
    [2] Paladin
    [3] Mago
    [4] Hechicero
    [5] Explorador
    [6] Batidor""")
opcion = int(input("Opcion> "))
while bucle:
    if opcion == 1:

        p1.setClase("Guerrero")
        tipoPersonaje = "Fisicos"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setIniciativa(randomIniciativaPersonaje)
        bucle = False
    elif opcion == 2:
        p1.clase = "Paladin"
        tipoPersonaje = "Fisicos"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setIniciativa(randomIniciativaPersonaje)
        bucle = False
    elif opcion == 3:
        p1.clase = "Mago"
        tipoPersonaje = "Magicos"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setIniciativa(randomIniciativaPersonaje)
        bucle = False
    elif opcion == 4:
        p1.clase = "Hechicero"
        tipoPersonaje = "Magicos"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setIniciativa(randomIniciativaPersonaje)
        bucle = False
    elif opcion == 5:
        p1.clase = "Explorador"
        tipoPersonaje = "Arqueros"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setIniciativa(randomIniciativaPersonaje)
        bucle = False
    elif opcion == 6:
        p1.clase = "Batidor"
        tipoPersonaje = "Arqueros"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setIniciativa(randomIniciativaPersonaje)
        bucle = False
    else:
        print("Introduce un numero valido")
        opcion = int(input("Opcion> "))
print(""" -- ELIGE UNA RAZA --
    [1] Humano
    [2] Elfo
    [3] Enano""")
opcion = int(input("Opcion> "))
bucle = True
while bucle:
    if opcion == 1:
        p1.raza = "Humano"
        bucle = False
    elif opcion == 2:
        p1.raza = "Elfo"
        bucle = False
    elif opcion == 3:
        p1.raza = "Enano"
        bucle = False
    else:
        print("Introduce un numero valido")
        opcion = int(input("Opcion> "))

p1.DatosPersonaje()
