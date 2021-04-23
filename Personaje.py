import random
import sys
import time

def imprimir_con_retraso(s):
    # Imprimiri una letra a la vez
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
class Personaje:
    def __init__(self, nombre, raza, clase, vida, escudo, ataque, iniciativa, tecnicas):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.vida = vida
        self.escudo = escudo
        self.ataque = ataque
        self.iniciativa = iniciativa
        self.vidaActual = vida
        self.tecnicas = tecnicas
        self.magico = "Magicos"
        self.fisico = "Fisicos"
        self.curandero = "Curanderos"
        self.arquero = "Arqueros"

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setRaza(self, raza):
        self.raza = raza

    def getRaza(self):
        return self.raza

    def setClase(self, clase):
        self.clase = clase

    def getClase(self):
        return self.clase

    def setVida(self, vida):
        self.vida = vida

    def getVida(self):
        return self.vida

    def setEscudo(self, escudo):
        self.escudo = escudo


    def getEscudo(self):
        return self.escudo

    def setAtaque(self, ataque):
        self.ataque = ataque

    def getAtaque(self):
        return self.ataque

    def setIniciativa(self, iniciativa):
        self.iniciativa = iniciativa

    def getIniciativa(self):
        return self.iniciativa

    def setTecnicas(self, tecnicas):
        self.tecnicas = tecnicas

    def AtaqueBase(self, tipo):
        ataquePorDefecto = 1
        if tipo == self.magico:
            return ataquePorDefecto + 3
        elif tipo == self.fisico:
            return ataquePorDefecto + 2
        elif tipo == self.curandero:
            return ataquePorDefecto
        elif tipo == self.arquero:
            return ataquePorDefecto + 2
        else:
            return "Error ataque"


    def VidaPersonaje(self, vida, tipo):
        if tipo == self.magico:
            return vida - 2
        elif tipo == self.fisico:
            return vida + 3
        elif tipo == self.curandero:
            return vida + 2
        elif tipo == self.arquero:
            return vida
        else:
            return "Error vida"

    def EscudoPersonaje(self, escudo, tipo):
        if tipo == "Magicos":
            return escudo - 2
        elif tipo == "Fisicos":
            return escudo + 3
        elif tipo == "Curanderos":
            return escudo + 2
        elif tipo == "Arqueros":
            return escudo
        else:
            return "Error escudo"

    def ApareceMousntro(self,nombre, raza, clase):
        print("¡" + nombre, "el", raza, "quiere pelear!")
        print("¡Vaya parece un", clase + "!")
        print("¡Prepara tus armas", self.nombre + " que se avecina el combate!")

    def SetNombrePersonaje(self,nombre):
        self.nombre = nombre
    def DatosPersonaje(self):
        print('--- FICHA DE TU PERSONAJE ---','\n'
            'NOMBRE:', self.nombre,'\n'
            'RAZA:', self.raza,'\n'
            'CLASE:', self.clase,'\n'
            'VIDA:', self.vida,'\n'
            'ESCUDO:', self.escudo,'\n'
            'ATAQUE BASE:', self.ataque,'\n'
            'INICIATIVA: ', self.iniciativa)

    def turno(self, monster, tecnicas):

        while self.vidaActual > 0:

            print(f"\n{self.nombre}\t\tVIDA:\t{self.vidaActual}")

            # Jugador
            print(f"Es hora de pelear {self.nombre}")
            for i, x in enumerate(tecnicas):
                print(f"{i + 1}.", x)
            index = int(input('Como quieres atacar: '))
            imprimir_con_retraso(f"\n¡{self.nombre} usó {tecnicas[index - 1]}!")
            time.sleep(1)

            # Saber daño
            entraDaño = random.choice(range(1, 20)) + self.ataque
            if entraDaño > monster.escudo:
                # Saber cuanto le has quitado
                monster.vidaActual -= self.ataque
                imprimir_con_retraso(f"\nBuen golpe, le has quitado {self.ataque} de daño")
                time.sleep(1)
                print("\n")
            else:
                imprimir_con_retraso(f"\nLo siento has sacado {entraDaño} no es suficiente para entrarle al monstruo")
                time.sleep(3)
                print("\n")

            # Monstruo muere
            if monster.vidaActual <= 0:
                imprimir_con_retraso("\n Eres todo un campeón " + monster.nombre + ' ha muerto.')
                break

            # Monstruo
            print("\n")
            imprimir_con_retraso(f"Es turno de {monster.nombre}")
            time.sleep(2)

            entraDaño = random.choice(range(1, 20)) + monster.ataqueBase
            if entraDaño > monster.escudo:
                ataquealeatorio = random.choice(monster.tecnicas)
                imprimir_con_retraso(f"\n¡{monster.nombre} usó {ataquealeatorio}!")
                # Saber cuanto le has quitado
                self.vidaActual -= monster.ataqueBase
                imprimir_con_retraso(f"\nTe ha dado un buen golpe, te ha quitado {monster.ataqueBase} de vida")
                time.sleep(1)
                print("\n")
            else:
                imprimir_con_retraso(f"\nQue suerte, el mounstruo no te ha podido pegar")
                time.sleep(3)
                print("\n")

            # Monstruo muere
            if self.vidaActual <= 0:
                imprimir_con_retraso("\nGame over " + self.nombre + ' ha muerto.')
                break

    def lucha(self, monster, tecnicas):
        self.turno(monster)
