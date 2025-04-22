print("mi calculadora en python")
#ingresar los numeros 
num1= float(input("ingresa el primer numero"))
num2= float(input("ingresa el segundo numero"))
#mostrar menu de operaciones
print("operaciones disponibles")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
operacion=input("elija una operacion")
#logica con: if/ elif /else
if operacion == "1":
    resultado = num1+num2
    print("resultado de la suma es:",resultado)
elif operacion == "2":
    resultado = num1-num2
    print("resultado de la resta es:",resultado)
elif operacion =="3":
    resultado = num1*num2
    print("resultado de la multiplicacion es:",resultado)
elif operacion == "4":
    resultado = num1/num2
    print("resultado de la division es:",resultado) 
else:
    print ("opcion no valida")

print ("¿desea seguir en la calculadora?")
print ("1. si")
print ("2. no")
continuar = input("ingresa la opcion")
if continuar =="1":
    print("se volvera a ejecutar la calculadora")
else:
    print ("gracias por usar mi calculadora")





