from Ninja import Ninja
import random

class Combat:
    def __init__(self,ninja1,ninja2):
        self.ninja1 = ninja1
        self.ninja2 = ninja2
        
    def turno_ataque(self, atacante, defensor):
        daño = max (1, atacante.estadisticas["ataque"] - defensor.estadisticas["defensa"])
        if atacante.lista_jutsus and atacante.estadisticas["chakra"] > 0:
            jutsu = random.choice(atacante.lista_jutsus)
            print(f"{atacante.nombre} usa {jutsu}!")
            atacante.estadisticas["chakra"] -= 1
        
        defensor.vida -= daño
        if defensor.vida < 0:
            defensor.vida = 0

        print(f"{atacante.nombre} ataca a {defensor.nombre} causando {daño} de daño. "
            f"Vida de {defensor.nombre}: {defensor.vida}")
        
    def iniciar_batalla(self):
        print(f"¡Comienza la batalla entre {self.ninja1.nombre} y {self.ninja2.nombre}!\n")

        turno = 0
        while self.ninja1.vida > 0 and self.ninja2.vida > 0:
            if turno % 2 == 0:
                self.turno_ataque(self.ninja1, self.ninja2)
            else:
                self.turno_ataque(self.ninja2, self.ninja1)
            turno += 1
        ganador = self.ninja1 if self.ninja1.vida > 0 else self.ninja2
        print(f"\n {ganador.nombre} ha ganado la batalla con {ganador.vida} de vida restante!")

