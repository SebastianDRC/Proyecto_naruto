from factory import KonohaFactory, SunaFactory, AkatsukiFactory
from Ninja import Ninja
from Combat import Combat

print("PRUEBA CREACION NINJA CON FABRICA CONCRETA")

konoha_factory = KonohaFactory()
suna_factory = SunaFactory()
akatsuki_factory = AkatsukiFactory()

naruto = konoha_factory.crear_ninja("Naruto")
gaara = suna_factory.crear_ninja("Gaara")
itachi = akatsuki_factory.crear_ninja("Itachi")

for ninja in [naruto, gaara, itachi]:
    print(f"Nombre: {ninja.nombre}")
    print(f"Aldea: {ninja.aldea}")
    print(f"Rango: {ninja.rango}")
    print(f"Estadísticas: {ninja.estadisticas}")
    print(f"Jutsus: {', '.join(ninja.lista_jutsus)}")

print("PRUEBA ENTRENAMIENTO")

print("Antes del entrenamiento:")
print(naruto.estadisticas)
print(itachi.estadisticas)

naruto.train()
itachi.train()

print("Después del entrenamiento:")
print(naruto.estadisticas)
print(itachi.estadisticas)


print("PRUEBA COMBATE")

batalla = Combat(naruto, itachi)
batalla.iniciar_batalla()
