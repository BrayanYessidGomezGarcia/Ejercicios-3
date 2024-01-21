import math 
denominador= 2
diferencia= 1 
e= 2
fra_anteriores= 1
fraccion= 1
while diferencia > 0.0001:
    fra_anteriores= fraccion 
    fraccion=1 / math.factorial(denominador)
    denominador +=1
    e += fraccion 
    diferencia= fra_anteriores- fraccion
print(e)
    