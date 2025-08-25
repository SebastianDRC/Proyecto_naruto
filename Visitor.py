import json

class VisitorExportar:
    def __init__(self):
        self.data = {"ninjas": [], "misiones": []}

    def visit_ninja(self, ninja):
        self.data["ninjas"].append({
            "nombre": ninja.nombre,
            "aldea": ninja.aldea,
            "rango": ninja.rango,
            "estadisticas": ninja.estadisticas,
            "jutsus": ninja.lista_jutsus,
            "vida": ninja.vida
        })

    def visit_mision(self, mision):
        self.data["misiones"].append({
            "nombre": mision.nombre,
            "rango": mision.rango_mision,
            "rango_requerido": mision.rango_requerido,
            "recompensas": {
                "ataque": mision.recompensa_ataque,
                "defensa": mision.recompensa_defensa,
                "chakra": mision.recompensa_chakra
            }
        })

    def exportar_a_json(self, archivo="exportacion.json"):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
