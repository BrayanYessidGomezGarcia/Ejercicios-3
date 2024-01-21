num= int(input("Escribe el numero de terminos: "))
suma= 0
signo= 1

for i in range(1, 2 * num + 1,2):
    termino= 4 * signo / i
    suma+= termino
    signo *= -1

print(f"La estimacion de n con {num} terminos es: {suma}")
