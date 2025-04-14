def factorial(numero):
    resultado = 1
    for i in range(2,numero+1):
        resultado *= i
        print(resultado)
        
facto = factorial(5)
print(facto)