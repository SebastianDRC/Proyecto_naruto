class Ninja:
    def __init__(self,nombre,aldea,rango,ataque,defensa,chakra,lista_jutsus=None,vida=100):
        self.nombre = nombre
        self.aldea = aldea 
        self.rango = rango
        self.estadisticas = {"ataque": ataque,"defensa" :defensa,"chakra": chakra}
        self.lista_jutsus = lista_jutsus
        self.vida = vida
        pass
    def train (self,ataque_train=1,defensa_train=1,chakra_train=1):
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