#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
num = 3
if num > 0:
    print("Mayor a cero")
elif num < 0:
    print("Menor a cero")
else:
    print("Igual a cero")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
nombre= "Rad"
edad= 26
if type(edad) == type(nombre):
    print("Variables de mismo tipo")
else:
    print("Variables de diferente tipo")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for i in range(1,21):
    if (i%2 == 0):
        print( str(i) + "es par")
    else:
        print(str(i) + "es impar")





# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(0, 6):
    print(i**3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
n= 10
for i in range(0, n):
    




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
n = 33
if type(n) == int:
    if n >0:
        while n > 1:
            a= n
            n= a * (n-1)
            n -=1
        print(n)
    else:
        print("No mayor a cero")
else:
    print("número no entero")


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
n = 0
while n < 7 :
    for i in range(2):
        print("Copa libertadores n°", i)
        n+=1





# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:





# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
for i in range(0,31):
    if i==0:
        print(f"N {i} es primo")
    j = i-1
    while j > 1:
        if i%j != 0:
            j-=1
            continue
        else:
            break
    if j == 1:
        print(f"N {i} es primo")





# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:




# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
n = 100
while n < 301:
    if n%12 == 0:
        print(n)
    n+=1




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
i= 0
while True:
    if i==0:
        print(f"N° {i} es primo")
        if (input("Apreta 1 si querés seguir:") != "1"):
            break
        else:
            i +=1
    j = i-1
    while j > 1:
        if (i%j) != 0:
            j-=1
            continue
        else:
            break
    if j <= 1:
        print(f"N° {i} es primo")
        if (input("Apreta 1 si querés seguir: ") != "1"):
            print("Programa finalizado")
            break
    i+=1




# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

n=100
flag = False
while n < 301:
    if n % 3 ==0:
        if n%6 ==0:
            print(f"{n} es divisible por 3 y múltiplo de 6")
            flag=True
    n+=1      
    if flag:
        break

