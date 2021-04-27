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
    def __init__(self, nombre, raza, clase, vida, escudo, ataque, iniciativa, tecnicas, daño):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.vida = vida
        self.escudo = escudo
        self.ataque = ataque
        self.iniciativa = iniciativa
        self.vidaActual = vida
        self.tecnicas = tecnicas
        self.daño = daño
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

    def setDaño(self, daño):
        self.daño = daño

    def getDaño(self):
        return self.daño

    def impresa(self, monster):
        print("----A PELEAR----")
        print(f"\n{self.nombre}")
        print("RAZA:", self.raza)
        print("CLASE:", self.clase)
        print("\nVS")
        print(f"\n{monster.nombre}")
        print("RAZA:", monster.raza)
        print("CLASE:", monster.clase)
        time.sleep(2)

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

    def DañoGolpeJugador(self, monster, index):

        entraDaño = random.choice(range(1, 21)) + self.ataque
        dado6 = random.choice(range(1, 7))
        dado8 = random.choice(range(1, 9))
        dado10 = random.choice(range(1, 11))
        if entraDaño > monster.escudo:
            if index == 1:
                daño = monster.ataque + dado10
            if index == 2:
                daño = monster.ataque + dado8
            if index == 3:
                daño = monster.ataque + dado6
            # Saber cuanto le has quitado
            monster.vidaActual -= daño
            imprimir_con_retraso(f"\nHas sacado {entraDaño}")
            imprimir_con_retraso(f"\nBuen golpe, le has quitado {daño} de daño")
            time.sleep(1)
            print("\n")
        else:
            imprimir_con_retraso(f"\nLo siento has sacado {entraDaño} no es suficiente para entrarle al monstruo")
            time.sleep(3)
            print("\n")

    def DañoGolpeMonster(self, monster):

        entraDaño = random.choice(range(1, 21)) + monster.ataque
        if entraDaño > self.escudo:
            dado6Monster = random.choice(range(1, 7))
            dado8Monster =  random.choice(range(1, 9))
            dado10Monster =  random.choice(range(1, 11))
            ataquealeatorio = random.choice(monster.tecnicas)
            indiceTecnicaM = monster.tecnicas.index(ataquealeatorio) + 1
            daño = 0
            if indiceTecnicaM == 1:
                daño = monster.ataque + dado10Monster

            if indiceTecnicaM == 2:
                daño = monster.ataque + dado8Monster

            if indiceTecnicaM == 3:
                daño = monster.ataque + dado6Monster
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
    def ApareceMousntro(self,nombre, raza, clase):
        print("¡" + nombre, "el", raza, "quiere pelear!")
        print("¡Vaya parece un", clase + "!")
        print("¡Prepara tus armas", self.nombre + " que se avecina el combate!")

    # def SetNombrePersonaje(self, nombre):
    #    self.nombre = nombre

    def DatosPersonaje(self):
        print('--- FICHA DE TU PERSONAJE ---','\n'
            'NOMBRE:', self.nombre,'\n'
            'RAZA:', self.raza,'\n'
            'CLASE:', self.clase,'\n'
            'VIDA:', self.vida,'\n'
            'ESCUDO:', self.escudo,'\n'
            'ATAQUE BASE:', self.ataque,'\n'
            'INICIATIVA: ', self.iniciativa)

    def turno(self, monster):

        while self.vidaActual > 0:
            print("VIDA MONSTER:",monster.vidaActual)
            corazones = emoji.emojize(":red_heart:",variant="emoji_type") * self.vidaActual

            print(f"\n{self.nombre} VIDA: {self.vidaActual} \n {corazones}")

            # Jugador
            print(f"Es hora de pelear {self.nombre}")
            for i, x in enumerate(self.tecnicas):
                print(f"{i + 1}.", x)
            index = int(input('Como quieres atacar: '))
            print(index)
            imprimir_con_retraso(f"\n¡{self.nombre} usó {self.tecnicas[index - 1]}!")
            time.sleep(1)
            self.DañoGolpeJugador(monster,index)
            # Saber daño
            # entraDaño = random.choice(range(1, 21)) + self.ataque
            # dado6 = random.choice(range(1, 7))
            # dado8 = random.choice(range(1, 9))
            # dado10 = random.choice(range(1, 11))
            # if entraDaño > monster.escudo:
            #     if index == 1:
            #         daño = monster.ataque + dado10
            #         print(daño)
            #         print("dado", dado10)
            #     if index == 2:
            #         daño = monster.ataque + dado8
            #         print(daño)
            #         print("dado", dado8)
            #     if index == 3:
            #         print(monster.ataque)
            #         daño = monster.ataque + dado6
            #         print(daño)
            #         print("dado", dado6)
            #     # Saber cuanto le has quitado
            #     monster.vidaActual -= self.ataque
            #     imprimir_con_retraso(f"\nBuen golpe, le has quitado {self.ataque} de daño")
            #     time.sleep(1)
            #     print("\n")
            # else:
            #     imprimir_con_retraso(f"\nLo siento has sacado {entraDaño} no es suficiente para entrarle al monstruo")
            #     time.sleep(3)
            #     print("\n")

            # Monstruo muere
            if monster.vidaActual <= 0:
                imprimir_con_retraso("\n Eres todo un campeón " + monster.nombre + ' ha muerto.')
                break

            # Monstruo
            print("\n")
            imprimir_con_retraso(f"Es turno de {monster.nombre}")
            time.sleep(2)
            self.DañoGolpeMonster(monster)
            # Monstruo muere
            if self.vidaActual <= 0:
                imprimir_con_retraso("\nGame over " + self.nombre + ' ha muerto.')
                break

    def lucha(self, monster):
        self.impresa(monster)
        self.turno(monster)
