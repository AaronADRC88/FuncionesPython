__author__ = 'aferreiradominguez'


def nome_funcion(param1, param2):
    """esta funcion imprime los valores de parametro"""
    print(param1)
    print(param2)


nome_funcion("o numero e: ", 5)
nome_funcion(param2="7", param1="Non e letra")


def printa(texto, veces=1):
    """imprime texto n veces"""
    print(veces * texto)


printa("lolololo", 5)
printa("titititititititititi", 6)
printa("una")


def variosParam(param1, param2, *outros):
    """parametros ilimitados"""
    print(param1)
    print(param2)
    print(*outros)
    for ele in outros:
        print(ele)


variosParam("lolo", 6, 5, 7, 9, 6, 3, 2, 1, 4, 5, 6, 7, 8, 6, 152, 14, 236, 14, "XD")


def varParam2(**outros):
    """2 o + param mais os nomes"""
    for ele in outros.items():
        print (ele)

    for clave in outros:
        print(clave, outros[clave])

varParam2(nome="YO",apelido="lololo")

