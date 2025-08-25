from Ninja import Ninja

class NinjaBuilder:
    def __init__(self):
        self.nombre = None
        self.aldea = None
        self.rango = None
        self.ataque = 0
        self.defensa = 0
        self.chakra = 0
        self.vida = 100
        self.jutsus = []

    def set_nombre(self, nombre):
        self.nombre = nombre
        return self

    def set_aldea(self, aldea):
        self.aldea = aldea
        return self

    def set_rango(self, rango):
        self.rango = rango
        return self

    def set_ataque(self, ataque):
        self.ataque = ataque
        return self

    def set_defensa(self, defensa):
        self.defensa = defensa
        return self

    def set_chakra(self, chakra):
        self.chakra = chakra
        return self

    def set_vida(self, vida):
        self.vida = vida
        return self

    def add_jutsu(self, jutsu):
        self.jutsus.append(jutsu)
        return self

    def build(self):
        return Ninja(
            nombre=self.nombre,
            aldea=self.aldea,
            rango=self.rango,
            ataque=self.ataque,
            defensa=self.defensa,
            chakra=self.chakra,
            lista_jutsus=self.jutsus,  
            vida=self.vida
        )
