# =================================================================
#     PROMEDIO SEMANAL DEL CLIMA (POO)
# =================================================================
# Incluye:
#  Encapsulamiento
#  Herencia
#  Polimorfismo
# =================================================================

# Clase base: RegistroClima (ABSTRACCIÓN)
class RegistroClima:
    def __init__(self):
        self._datos = []  # Encapsulamiento

    def agregar_dato(self, valor):
        self._datos.append(valor)

    def calcular_promedio(self):
        if len(self._datos) == 0:
            return 0
        return sum(self._datos) / len(self._datos)

# Clase hija: ClimaSemanal (HERENCIA)
class ClimaSemanal(RegistroClima):
    def __init__(self):
        super().__init__()
        self.dias = [
            "Lunes", "Martes", "Miércoles", "Jueves",
            "Viernes", "Sábado", "Domingo"
        ]

    # POLIMORFISMO: redefine cómo se ingresan datos
    def ingresar_temperaturas(self):
        print("=== Ingreso de temperaturas de la semana (POO versión 2) ===")
        for dia in self.dias:
            valor = float(input(f"Ingrese temperatura del {dia}: "))
            self.agregar_dato(valor)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal registrado es: {promedio:.2f} °C")

# Programa principal
def main():
    registro = ClimaSemanal()
    registro.ingresar_temperaturas()
    registro.mostrar_promedio()

if __name__ == "__main__":
    main()
