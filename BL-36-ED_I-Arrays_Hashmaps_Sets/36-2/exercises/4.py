"""
Dado dois arrays de números inteiros que representam instantes de entrada e
saídas em uma biblioteca e um número que represente um instante a ser buscado.
Retorne quantas pessoas estudantes estão na biblioteca naquele instante.
Considere que todo estudante que entrou, saiu da biblioteca.

entradas = [1, 2, 3]
saídas = [3, 2, 7]
instante_buscado = 4
resultado: 1

O estudante 1 entrou no instante 1 e saiu no 3, já o segundo entrou
e saiu no 2 e o último foi único a estar presente no instante 4.
"""


def search_instant(enter, exit, instant):
    students = []
    size = len(enter)
    index = 0

    for index in range(size):
        students.append({index: [enter[index], exit[index]]})
        index += 1

    print(students)
