def calcularpago(horas, tarifa):
    MAX_HORAS = 40
    if (int(horas) > MAX_HORAS):
        horas_extras = int(horas) - MAX_HORAS
    else:
        horas_extras = 0
    calculo = (int(horas) * int (tarifa)) + (horas_extras * (int(tarifa) / 2))
    return calculo

horas = input("Ingrese número de horas: ")
tarifa = input("Ingrese tarifa: ")
pago = calcularpago (horas, tarifa)
print(pago)