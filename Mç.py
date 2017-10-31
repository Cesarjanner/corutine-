def letras_generador():

    yield "Imprimir letras de la a a la m"

    inicial = 'a'
    while inicial <= 'm':
        yield inicial
        inicial = chr(ord(inicial)+1)
for letras in letras_generador():



    print(letras)


