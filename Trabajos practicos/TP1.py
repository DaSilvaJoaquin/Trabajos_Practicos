#Ejercicio 5
romano = {"i": 1, "v": 5, "x": 10, "l": 50, "c":100, "d":500, "m":1000}
numero=input("Ingrese un numero romano a convertir\n")
def romano_to_decimal(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    else:
        if romano[numero_romano[0]] >= romano[numero_romano[1]]:
            return romano[numero_romano[0]] + romano_to_decimal(numero_romano[1:])
        else:
            return - romano[numero_romano[0]] + romano_to_decimal(numero_romano[1:])

print(romano_to_decimal(numero))


#Ejercicio 22
cantidad_objetos_sacados= 0
mochila1=['arroz ','pan' ,'Sable de luz' ]
def usar_la_fuerza(mochila,pos):
    
    if len(mochila)==0:
        return 'No hay mas objetos en la mochila'
    else :
        if mochila[0]=='Sable de luz' :
                     return print('El sable de luz se encontro en ',pos+1)
        else:                    
            return usar_la_fuerza(mochila[:1],pos+1)

print(usar_la_fuerza(mochila1,cantidad_objetos_sacados))        


