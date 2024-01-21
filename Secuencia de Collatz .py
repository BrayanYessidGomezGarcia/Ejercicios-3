num= int(input("Ingrese un mumero: "))
for i in range(num): 
 if num % 2 ==0:
    print(i/2)
 if i %2 ==1:
    print((i*3)+1)
 elif(i == 1):
    print("La funcion ha terminado")

else:
 print("Error")  

