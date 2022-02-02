"""
Sua trajetória no curso foi um sucesso e agora você está trabalhando para a
Trybe! Em um determinado módulo, os estudantes precisam entregar dois
trabalhos para seguir adiante. Cada vez que um dos trabalhos é entregue, o
nome da pessoa fica registrado. Precisamos saber como está o andamento da
entrega das listas. Para isso, você tem acesso aos nomes das pessoas da turma,
bem como ao log de quem já entregou qual lista. A partir das listas abaixo,
crie quatro funções que respondem às perguntas a seguir.
"""

"""
estudantes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
lista1_entregues = ['a', 'd', 'g', 'c']
lista2_entregues = ['c', 'a', 'f']
"""


# Quem ainda não entregou a lista1?
def not_done_list1(students, list1):
    log = set(students)
    result = log.difference(list1)
    return result


# Quem já entregou as duas listas?
def all_done(list1, list2):
    log = set(list1)
    result = log.intersection(list2)
    return result


# Quem já entregou qualquer uma das duas listas?
def one_done(list1, list2):
    log = set(list1)
    result = log.symmetric_difference(list2)
    return result


# Quem ainda não entregou nenhuma das listas?
def done_nothing(students, list1, list2):
    nothing_done = []
    for student in students:
        if student not in list1 and student not in list2:
            nothing_done.append(student)

    return nothing_done
