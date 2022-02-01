"""
Em um software monitor, que verifica a resiliência de outro software,
precisamos saber qual o tempo máximo que um software permaneceu sem
instabilidades. Para isto, a cada hora é feito uma requisição ao
sistema e verificamos se está ok. Supondo um array que contenha os
estados coletados por nosso software, calcule quanto tempo máximo
que o servidor permaneceu sem instabilidades.
"""

"""
1 - OK
0 - Instabilidades

valores_coletados1 = [0, 1, 1, 1, 0, 0, 1, 1]
resultado = 3

valores_coletados2 = [1, 1, 1, 1, 0, 0, 1, 1]
resultado = 4
"""

valores_coletados1 = [0, 1, 1, 1, 0, 0, 1, 1]
valores_coletados2 = [1, 1, 1, 1, 0, 0, 1, 1]


def sum_values(list):
    result = list.count(1)

    return result


print(
    f"O total sem instabilidade(s) é: {sum_values(valores_coletados1)}"
)
