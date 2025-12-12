# =================================================================
#     PROMEDIO SEMANAL DEL CLIMA (VERSIÓN TRADICIONAL)
# =================================================================
# Enfoque: Programación estructurada
# Característica: Uso claro de funciones independientes
# =================================================================

# Función para solicitar las temperaturas diarias
def leer_temperaturas_semanales():
    print("=== Registro de temperaturas (Tradicional 2) ===")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    valores = []

    for nombre_dia in dias:
        temp = float(input(f"Ingrese temperatura del {nombre_dia}: "))
        valores.append(temp)

    return valores

# Función que calcula el promedio
def promedio(valores):
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

# Función principal
def main():
    temperaturas = leer_temperaturas_semanales()
    prom = promedio(temperaturas)
    print(f"\nEl promedio semanal del clima es: {prom:.2f} °C")

if __name__ == "__main__":
    main()

