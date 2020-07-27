#Escribir un programa llamado prog3.py que muestre al usuario el siguiente menu.

while True:
    print ("Operaciones\n S. Suma\n R. Resta\n M. Multiplicacion\n D. Division\n A. Salir")
        
    respuesta = input("Elige una opcion: ").upper()
    if respuesta == "S" or respuesta == "R" or respuesta == "M" or respuesta == "D":

        numero1 = int(input("Dame tu primer numero a resolver: "))
        numero2 = int(input("Dame tu segundo numero a resolver: "))

        if respuesta == "S":
            print(f"El resultado de la suma de tus numeros ingresados es: {numero1 + numero2}")

        elif respuesta == "R":
            print(f"El resultado de la resta de tus numeros ingresados es: {numero1 - numero2}")

        elif respuesta == "M":
            print(f"El resultado de la multiplicacion de tus numeros ingresados es: {numero1 * numero2}")
    
        elif respuesta == "D":
            print(f"El resultado de la division de tus numeros ingresados es: {numero1 / numero2}")

    elif respuesta == "A":
            print("     CERRANDO EL PROGRAMA MENU DE OPERACIONES     ")
            print("     HASTA PRONTO........     ")
            break
    
        

    















     