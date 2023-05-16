# uso del WHILE 
    # repeticion 
n = 1
while n <= 10:
    print (n)
    n += 1

print("________________")
# repeticion con break
x=1
while x <= 10:
    print(x)
    
    if ( x==5):
        print("Es la mitas")
        break

    x += 1

print("_______________")
# repeticion con continue 
x=0
while x <= 10:
    x += 1
       
    if ( x==5):
        continue

    print(x) 
    
print("__________")
# suma de numeros naturales  
m = int(input("Indroduce un numero para la suma hasta el :)"))
suma = 0
while(m > 0):
    suma += m 
    print(suma)
    m = m - 1
print(suma)

