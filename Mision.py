from Ninja import Ninja

class Mision:
    def __init__(self, nombre, rango_requerido, recompensa_ataque, recompensa_defensa, recompensa_chakra):
        self.nombre = nombre
        self.rango_requerido = rango_requerido
        self.recompensa_ataque = recompensa_ataque
        self.recompensa_defensa = recompensa_defensa
        self.recompensa_chakra = recompensa_chakra

    def asignar_a(self, ninja):
        if ninja.rango == self.rango_requerido:
            ninja.estadisticas["ataque"] += self.recompensa_ataque
            ninja.estadisticas["defensa"] += self.recompensa_defensa
            ninja.estadisticas["chakra"] += self.recompensa_chakra
            return f"{ninja.nombre} completó la misión {self.nombre} "
        else:
            return f"{ninja.nombre} no puede aceptar la misión {self.nombre}  (Requiere rango {self.rango_requerido})"


# ---------------- PRUEBAS ----------------

# Creamos un ninja
naruto = Ninja("Naruto", "Konoha", "Genin", 50, 40, 60, ["Rasengan"], 100)

# Creamos misiones
mision1 = Mision("Recolectar hierbas", "Genin", 5, 3, 2)
mision2 = Mision("Proteger al señor feudal", "Chunin", 10, 8, 6)

# Prueba 1: Naruto intenta la misión 1 (sí cumple con el rango)
print(mision1.asignar_a(naruto))
print("Estadísticas después de la misión 1:", naruto.estadisticas)

# Prueba 2: Naruto intenta la misión 2 (no cumple con el rango)
print(mision2.asignar_a(naruto))
print("Estadísticas después de la misión 2:", naruto.estadisticas)

