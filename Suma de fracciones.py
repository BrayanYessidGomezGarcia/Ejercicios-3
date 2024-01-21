fraccion = 1
i= 1
sum= 0
pfs= ["Potencia","Fraccion","Suma"]
for pfs in pfs: 
    print(pfs, end= "")
print("")
while fraccion > 0.000001:
    fraccion = 1/(2**i)
    sum += fraccion 
    print (str(i).ljust(8), end ="")
    print (str(round(fraccion, 4)).ljust(8), end="")
    print(round(sum,4))
    i+= 1 
    

     