def calcular_pago(dia, tiempo):
    tarifas = {
        "Lunes": 2.00, "Martes": 2.00, "Miércoles": 2.00,
        "Jueves": 2.50, "Viernes": 2.50,
        "Sábado": 3.00, "Domingo": 3.00
    }
    if dia not in tarifas:
        return "Día no válido"
    
    horas = int(tiempo)
    fraccion = 1 if (tiempo - horas) * 60 > 5 else 0
    total_pago = (horas + fraccion) * tarifas[dia]
    return total_pago

dia_semana = input("Ingrese el día de la semana: ")
tiempo = float(input("Ingrese el tiempo de estacionamiento en horas: "))

pago = calcular_pago(dia_semana, tiempo)
print("El monto a pagar es: $" + str(pago) if isinstance(pago, float) else pago)
