total_minutos= 0

while True: 
    time_input= int(input("Ingrese el tiempo de viaje: "))
    if time_input == 0: 
        break
    
    total_minutos += time_input
    
horas= total_minutos // 60
minutos= total_minutos % 60

print(f"El tiempo total de viaje es: {horas} horas: {minutos} minutos") 