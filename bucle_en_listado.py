def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    textos = ["Anita lava la tina", "Martin", "Ana", "luz AZul", "Pepito"]

    for texto in textos:
        es_palindromo = palindromo(texto)
        if es_palindromo == True:
            print(texto + " | Es palindromo")
        else:
            print(texto + " | No es palindromo")


if __name__ ==  '__main__':
    run()