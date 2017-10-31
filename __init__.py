def Numero_Impares():
    yield "Numeros"
    yield "Primos"


def generar_secuencua():
    numero = 1
    while True:
        yield numero
        numero = numero + 2

if __name__ == "__main__":
 generador = Numero_Impares()
 print(next(generador))

numeros = generar_secuencua()
for n in numeros:
    print (n)
    if n>198:
        break


