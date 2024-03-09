#Desarrollo de Función para Calcular Temperaturas Promedio en Python
def temperatura_promedio_ciudades(datos):
    promedios = {}

    for ciudad, temperaturas_semanas in datos.items():
        total_temperaturas_celsius = 0
        cantidad_temperaturas = 0

        for semana in temperaturas_semanas:
            total_temperaturas_celsius += sum(semana)
            cantidad_temperaturas += len(semana)

        promedios[ciudad] = {
            'celsius': total_temperaturas_celsius / cantidad_temperaturas,
            'kelvin': (total_temperaturas_celsius / cantidad_temperaturas) + 273.15,
            'fahrenheit': total_temperaturas_celsius * 9 / 5 + 32 / cantidad_temperaturas
        }

    return promedios


# Ejemplo de datos de 3 ciudades durante 4 semanas
datos_temperaturas = {
    'Ciudad1': [[20, 25, 22, 24], [23, 21, 26, 24], [25, 27, 23, 22], [20, 26, 24, 21]],
    'Ciudad2': [[18, 20, 22, 19], [21, 23, 25, 20], [19, 24, 23, 21], [22, 20, 23, 25]],
    'Ciudad3': [[15, 17, 16, 18], [18, 16, 15, 20], [19, 17, 16, 18], [20, 19, 21, 18]]
}

resultado = temperatura_promedio_ciudades(datos_temperaturas)
print(resultado)