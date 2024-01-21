num_terminos = int(input("Ingrese el número de términos para la estimación de pi: "))

if num_terminos <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    suma = 0
    signo = 1

    for i in range(1, num_terminos * 2, 2):
        termino = 1 / i * signo
        suma += termino
        signo *= -1

    valor_pi = 4 * suma
    print(f"La estimación de pi con {num_terminos} términos es: {valor_pi}")
