from Ninja import Ninja
import random

LISTA_JUTSUS = [
    "Mae Geri",
    "Konoha Senpuu",
    "Kaneten",
    "Ryuage Rendan",
    "Asshou",
    "Tsutenkyaku",
    "Chakra Tonkachi",
    "Omote Renge"
]

LISTA_RANGOS = [
    "Genin",
    "Chūnin",
    "Jōnin"
]

class KonohaFactory:
    def crear_ninja(self,nombre):
        jutsus_random = random.sample(LISTA_JUTSUS, random.randint(2, 4))
        rango_random = random.choice(LISTA_RANGOS)
        return Ninja(
            nombre=nombre,
            aldea="Konoha",
            rango=rango_random,
            ataque=random.randint(10, 20),
            defensa=random.randint(8, 15),
            chakra=random.randint(15, 25),
            lista_jutsus=jutsus_random
        )

class SunaFactory:
    def crear_ninja(self,nombre):
        jutsus_random = random.sample(LISTA_JUTSUS, random.randint(2, 4))
        rango_random = random.choice(LISTA_RANGOS)
        return Ninja(
            nombre=nombre,
            aldea="Suna",
            rango=rango_random,
            ataque=random.randint(10, 18),
            defensa=random.randint(10, 18),
            chakra=random.randint(15, 25),
            lista_jutsus=jutsus_random
        )

class AkatsukiFactory:
    def crear_ninja(self,nombre):
        jutsus_random = random.sample(LISTA_JUTSUS, random.randint(2, 4))
        rango_random = random.choice(LISTA_RANGOS)
        return Ninja(
            nombre=nombre,
            aldea="Akatsuki",
            rango=rango_random,
            ataque=random.randint(18, 25),
            defensa=random.randint(8, 15),
            chakra=random.randint(20, 30),
            lista_jutsus=jutsus_random
        )