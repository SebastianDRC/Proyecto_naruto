class Ninja:
    def __init__(self,nombre,aldea,rango,ataque,defensa,chakra,lista_jutsus=None,vida=100):
        self.nombre = nombre
        self.aldea = aldea 
        self.rango = rango
        self.estadisticas = {"ataque": ataque,"defensa" :defensa,"chakra": chakra}
        self.lista_jutsus = lista_jutsus
        self.vida = vida
        pass
    def train (self,ataque_train=3,defensa_train=2,chakra_train=5):
        self.estadisticas["ataque"] += ataque_train
        self.estadisticas["defensa"] += defensa_train
        self.estadisticas["chakra"] += chakra_train
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Aldea: {self.aldea}")
        print(f"Rango: {self.rango}")
        print(f"Vida: {self.vida}")
        print("Estadísticas:")
        for stat, valor in self.estadisticas.items():
            print(f"  {stat.capitalize()}: {valor}")
        print("Jutsus:")
        if self.lista_jutsus:
            for jutsu in self.lista_jutsus:
                print(f"  - {jutsu}")
        else:
            print("  (No tiene jutsus)")

    def __str__(self):
        """Representación legible al usar print()"""
        return (f"Ninja(nombre={self.nombre}, aldea={self.aldea}, rango={self.rango}, "
                f"ataque={self.estadisticas['ataque']}, defensa={self.estadisticas['defensa']}, "
                f"chakra={self.estadisticas['chakra']}, vida={self.vida}, "
                f"jutsus={self.lista_jutsus})")

    def __repr__(self):
        """Representación en Jupyter / consola interactiva"""
        return self.__str__()
