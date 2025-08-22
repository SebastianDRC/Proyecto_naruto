class Ninja:
    def __init__(self,nombre,rango,ataque,defensa,chakra,lista_jutsus=None):
        self.nombre = nombre
        self.rango = rango
        self.estadisticas = {ataque,defensa,chakra}
        self.lista_jutsus = lista_jutsus
        pass



