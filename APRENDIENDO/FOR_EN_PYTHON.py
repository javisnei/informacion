# fOR ES PARA LISTAS, TUPLAS Y DICCIONARIO

Lista = [1,2,3,4,5]

#FOR CON LISTAS 
for x in Lista :
    print(x)

print("__________________________")

#FOR CON BREAK 
for x in Lista:
    print(x)    
    if x == 3:
       break

print("__________________________")
#FOR CON  EXCEPCIONES 

for x in Lista:
    if x == 4:
        print(x+2)
        break

    print(x)

print("__________________________")
#FOR REPETICIONES 
numero = 5 
dis = 0
for x in range(numero):
    print(numero + dis)
    dis = dis-1
else:
    print("Eso es todo ")



n = 10
suma =0 
while(n > 1):
    suma +=  n 
    n = n-1
    

print(suma)


