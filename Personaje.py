import os
import random
import sys
import time
import emoji as emoji
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

    def setVidaActual(self):
        self.vidaActual = self.vida
        return self.vidaActual
    def getVidaActual(self):
        return self.vidaActual

    def setTecnicas(self, tecnicas):
        self.tecnicas = tecnicas
    def getTecnicas(self):
        return self.tecnicas
        return self.tecnicas

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

    def DatosPersonaje(self):

        print("---FICHA DE TU PERSONAJE---")
        imprimir_con_retraso(f"NOMBRE:  {self.nombre}\n"
                             f"CLASE:  {self.clase}\n"
                             f"RAZA:  {self.raza}\n"
                             f"VIDA:  {self.vida}\n"
                             f"ESCUDO:  {self.escudo}\n"
                             f"ATAQUE BASE:  {self.ataque}\n"
                             f"INICIATIVA:  {self.iniciativa}\n"
                             )
    def ApareceMousntro(self, monster):
        print("\n \n")
        time.sleep(2.5)
        imprimir_con_retraso(f"¡{monster.nombre}, el {monster.raza}, quiere pelear!\n")
        time.sleep(1)
        imprimir_con_retraso(f"¡Vaya parece un {monster.clase}!\n")
        time.sleep(1)
        imprimir_con_retraso(f"¡Prepara tus armas {self.nombre} que se avecina el combate!\n")

    def Corazones(self):
        corazones = emoji.emojize(":red_heart:", variant="emoji_type") * self.vidaActual
        imprimir_con_retraso(f"\n{self.nombre} VIDA: {self.vidaActual}\n{corazones}\n")

    def DadoPrioridadAccion(self):
        dj = random.choice(range(1, 21))
        dm = random.choice(range(1, 21))

        while dj == dm:
            dj = random.choice(range(1, 21))
            dm = random.choice(range(1, 21))
        return dj, dm

    def DañoGolpeJugador(self, monster):
        self.Corazones()
        print(f"¡Es tu turno {self.nombre}!")
        for i, x in enumerate(self.tecnicas):
            time.sleep(0.5)
            imprimir_con_retraso(f"{i + 1}. {x}\n")
        index = int(input("Como quieres atacar: "))

        imprimir_con_retraso(f"\n¡{self.nombre} usó {self.tecnicas[index - 1]}!")
        time.sleep(1)
        entraDaño = random.choice(range(1, 21)) + self.ataque
        dado4 = random.choice(range(1, 5))
        dado6 = random.choice(range(1, 7))
        dado8 = random.choice(range(1, 9))
        if entraDaño > monster.escudo:
            if index == 1:
                daño = self.ataque + dado8
            if index == 2:
                daño = self.ataque + dado6
            if index == 3:
                daño = self.ataque + dado4
            # Saber cuanto le has quitado
            monster.vidaActual -= daño
            imprimir_con_retraso(f"\nHas sacado {entraDaño}")
            imprimir_con_retraso(f"\nBuen golpe, le has quitado {daño} de vida")
            time.sleep(1)
            print("\n")
        else:
            imprimir_con_retraso(f"\nLo siento has sacado {entraDaño} no es suficiente para entrarle al monstruo")
            time.sleep(3)
            print("\n")

    def DañoGolpeMonster(self, monster):
        print("\n")
        imprimir_con_retraso(f"Es turno de {monster.nombre}")
        time.sleep(2)
        entraDaño = random.choice(range(1, 21)) + monster.ataque

        if entraDaño > self.escudo:

            dado4Monster = random.choice(range(1, 11))
            dado6Monster = random.choice(range(1, 7))
            dado8Monster = random.choice(range(1, 9))
            ataquealeatorio = random.choice(monster.tecnicas)
            indiceTecnicaM = monster.tecnicas.index(ataquealeatorio) + 1
            daño = 0

            if indiceTecnicaM == 1:
                daño = monster.ataque + dado4Monster

            if indiceTecnicaM == 2:
                daño = monster.ataque + dado6Monster

            if indiceTecnicaM == 3:
                daño = monster.ataque + dado8Monster
            imprimir_con_retraso(f"\n¡{monster.nombre} usó {ataquealeatorio}!")
            # Saber cuanto le has quitado
            self.vidaActual -= daño

            imprimir_con_retraso(f"\nTe ha dado un buen golpe, te ha quitado {daño} de vida")
            time.sleep(1)
            print("\n")
        else:
            imprimir_con_retraso(f"\nQue suerte, el mounstruo no te ha podido pegar")
            time.sleep(3)
            print("\n")

    def turno(self, monster):
        iniciativaP = self.iniciativa
        iniciativaM = monster.iniciativa
        while self.vidaActual >= 0:
            if self.iniciativa != monster.iniciativa:
                if self.iniciativa > monster.iniciativa:
                    self.DañoGolpeJugador(monster)
                    # Monster muere
                    if monster.vidaActual <= 0:
                        os.system("cls")
                        imprimir_con_retraso("\n Eres todo un campeón " + monster.nombre + ' ha muerto.')
                        break
                    else:
                        self.DañoGolpeMonster(monster)
                else:
                    self.DañoGolpeMonster(monster)
                    if self.vidaActual <= 0:
                        imprimir_con_retraso("\nGame over " + self.nombre + ' has muerto.')
                    else:
                        self.DañoGolpeJugador(monster)
            else:
                x = random.choice(range(2))
                if x == 0:
                    self.iniciativa += 1
                else:
                    monster.iniciativa += 1
        monster.iniciativa = iniciativaM
        self.iniciativa = iniciativaP
    def lucha(self, monster):
        self.DatosPersonaje()
        self.ApareceMousntro(monster)
        self.turno(monster)
