import numpy as np

def resolver_circuito(voltajes, resistencias):
    matriz_coeficientes = np.array([
        [resistencias[0], -resistencias[1], 0],
        [-resistencias[1], resistencias[1] + resistencias[2] + resistencias[3], -resistencias[3]],
        [0, -resistencias[3], resistencias[3] + resistencias[4] + resistencias[5]]
    ])

    vector_terminos = np.array([voltajes[0], 0, -voltajes[2]])

    corrientes = np.linalg.solve(matriz_coeficientes, vector_terminos)

    tensiones_resistores = corrientes * resistencias[1:4]

    return corrientes, tensiones_resistores

def obtener_valor(mensaje):
    valor = input(f"{mensaje}: ")
    while not valor:  # Mientras no se ingrese nada, solicitar nuevamente el valor
        print("No ingresaste un valor válido. Por favor, ingrésalo nuevamente.")
        valor = input(f"{mensaje}: ")
    return float(valor)

def imprimir_corrientes_mallas(corrientes):
    print("\nCorrientes en las mallas:")
    for i, corriente in enumerate(corrientes, start=1):
        print(f"Malla {i}: {corriente:.2f} A")

def imprimir_tensiones_resistores(tensiones_resistores):
    print("\nTensiones en los resistores:")
    for i, tension in enumerate(tensiones_resistores, start=2):
        print(f"Resistor {i}: {tension:.2f} V")

resistencias = [obtener_valor(f"Ingrese el valor de la resistencia {i + 1}") for i in range(6)]
voltajes = [obtener_valor(f"Ingrese el valor del voltaje {i + 1}") for i in range(3)]

corrientes, tensiones_resistores = resolver_circuito(voltajes, resistencias)

imprimir_corrientes_mallas(corrientes)
imprimir_tensiones_resistores(tensiones_resistores)
