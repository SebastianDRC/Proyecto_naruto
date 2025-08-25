from Mision import Mision
from factory import KonohaFactory, SunaFactory, AkatsukiFactory
from Ninja import Ninja
from Combat import Combat
from builder import NinjaBuilder

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

print("PRUEBA MISION")

# Crear ninjas
naruto = Ninja("Naruto", "Konoha", "Genin", 50, 40, 60, ["Rasengan"])
sasuke = Ninja("Sasuke", "Konoha", "Chunin", 55, 45, 70, ["Chidori"])
kakashi = Ninja("Kakashi", "Konoha", "Jonin", 80, 75, 90, ["Raikiri"])

# Crear misiones
mision_d = Mision("Recolectar hierbas", "D", "Genin", 5, 3, 2)
mision_c = Mision("Escoltar comerciante", "C", "Chunin", 10, 5, 4)
mision_a = Mision("Proteger al Hokage", "A", "Jonin", 20, 15, 10)

# Probar misiones
print(mision_d.asignar_a(naruto))   
print(mision_c.asignar_a(naruto))   
print(mision_c.asignar_a(sasuke))   
print(mision_a.asignar_a(kakashi))  

# Mostrar resultados finales
print("\n=== Estadísticas finales ===")
naruto.mostrar_informacion()


print("\nPRUEBA BUILDER")
sasuke = (
    NinjaBuilder()
    .set_nombre("Sasuke")
    .set_aldea("Konoha")
    .set_rango("Chunin")
    .set_ataque(25)
    .set_defensa(20)
    .set_chakra(30)
    .add_jutsu("Chidori")
    .add_jutsu("Sharingan")
    .build()
)

print(sasuke)
