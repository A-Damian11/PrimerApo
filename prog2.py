#Escribir un programa que pida al usuario 2 numeros enteros y
#calcular la suma desde el numero 1 hasta el numero 2.
#imprimir el resultado de la suma

suma = 0
print ("Programa que muestra la suma de el numero1 hasta el 2")
num1 = int(input("Ingrese el primer numero:\n "))
num2 = int(input("Ingrese el segundo numero:\n "))
num2 = num2 + 1
for num in range (num1,num2):
    suma += num

print (f'El resultado es:\n {suma}')



