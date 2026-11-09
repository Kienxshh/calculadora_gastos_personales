def calcular_total(gasto1, gasto2, gasto3):
    return gasto1 + gasto2 + gasto3


def calcular_promedio(total, cantidad):
    return total / cantidad 

def clasificar_gasto(total):
    if total <= 5000:
        return "Gasto Bajo"
    elif total <= 10000:
        return "Gasto Moderado"
    else:
        return "Gasto elevado"

    
    