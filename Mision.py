from Ninja import Ninja

class Mision:
    def __init__(self, nombre, rango_mision, rango_requerido, recompensa_ataque, recompensa_defensa, recompensa_chakra):
        self.nombre = nombre
        self.rango_mision = rango_mision      
        self.rango_requerido = rango_requerido  
        self.recompensa_ataque = recompensa_ataque
        self.recompensa_defensa = recompensa_defensa
        self.recompensa_chakra = recompensa_chakra

    def asignar_a(self, ninja):
        if ninja.rango == self.rango_requerido:
            ninja.estadisticas["ataque"] += self.recompensa_ataque
            ninja.estadisticas["defensa"] += self.recompensa_defensa
            ninja.estadisticas["chakra"] += self.recompensa_chakra
            return f"{ninja.nombre} completó la misión {self.nombre} (Rango {self.rango_mision})", True
        else:
            return f"{ninja.nombre} no puede aceptar la misión {self.nombre} (Requiere rango {self.rango_requerido})", False

