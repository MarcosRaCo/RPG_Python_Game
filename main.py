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
                  "Curanderos": ["Gracia Divina", "Inflinjir Heridas", "Mazazo"],
                  "Arqueros": ["Abocajarro", "Disparo Rapido", "Disparo Penetrante"]
                  }
tipos = []
for tipo in clasesEnemigos.keys():
    tipos.append(tipo)
tipoMousntro = random.choice(tipos)

tiposTecnica = []
for tipo in tecnicas.keys():
    tiposTecnica.append(tipo)
tipoTecMonster = random.choice(tiposTecnica)
tecnicaMonster = random.choice(tecnicas[tipoTecMonster])

#Randoms Personaje
randomVidaPersonaje = random.choice(range(30, 50))
randomEscudoPersonaje = random.choice(range(1, 2))
randomIniciativaPersonaje = random.choice(range(1, 5))

#Randoms Monster
nombreMousntro = random.choice(nombresEnemigos)
razaMousntro = random.choice(razasEnemigos)
clase = random.choice(clasesEnemigos[tipoMousntro])
randomVidaMousntro = random.choice(range(15, 20))
randomEscudoMousntro = random.choice(range(1, 2))
randomIniciativaMonster = random.choice(range(1, 5))

m = Personaje(nombreMousntro, razaMousntro, clase, 0, 0, 0, randomIniciativaMonster, "", 0)
m.setVida(m.VidaPersonaje(randomVidaMousntro, tipoMousntro))
m.setEscudo(m.EscudoPersonaje(randomEscudoMousntro, tipoMousntro))
m.setAtaque(m.AtaqueBase(tipoMousntro))
m.setTecnicas(tecnicas.get(tipoMousntro))


tipoPersonaje = ""
p1 = Personaje("", "", "", 0, 0, 0, 0, "", 0)
p1.setTecnicas(tecnicas.get(tipoMousntro))
p1.setIniciativa(randomIniciativaPersonaje)

p1.nombre = input("Nombre de personaje: ")

print(""" -- ELIGE TU CLASE --
    [1] Guerrero
    [2] Paladin
    [3] Mago
    [4] Hechicero
    [5] Explorador
    [6] Batidor""")
opcion = int(input("Opcion> "))
bucle = True
while bucle:
    if opcion == 1:
        p1.setClase("Guerrero")
        tipoPersonaje = "Fisicos"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setTecnicas(tecnicas.get(tipoPersonaje))
        bucle = False
    elif opcion == 2:
        p1.setClase("Paladin")
        tipoPersonaje = "Fisicos"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setTecnicas(tecnicas.get(tipoPersonaje))
        bucle = False
    elif opcion == 3:
        p1.setClase("Mago")
        tipoPersonaje = "Magicos"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setTecnicas(tecnicas.get(tipoPersonaje))
        bucle = False
    elif opcion == 4:
        p1.setClase("Hechicero")
        tipoPersonaje = "Magicos"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setTecnicas(tecnicas.get(tipoPersonaje))
        bucle = False
    elif opcion == 5:
        p1.setClase("Explorador")
        tipoPersonaje = "Arqueros"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setTecnicas(tecnicas.get(tipoPersonaje))
        bucle = False
    elif opcion == 6:
        p1.setClase("Batidor")
        tipoPersonaje = "Arqueros"
        p1.setAtaque(p1.AtaqueBase(tipoPersonaje))
        p1.setVida(p1.VidaPersonaje(randomVidaPersonaje, tipoPersonaje))
        p1.setEscudo(p1.EscudoPersonaje(randomEscudoPersonaje, tipoPersonaje))
        p1.setTecnicas(tecnicas.get(tipoPersonaje))
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

p1.setVidaActual()
m.setVidaActual()
#p1.DatosPersonaje()

p1.lucha(m)