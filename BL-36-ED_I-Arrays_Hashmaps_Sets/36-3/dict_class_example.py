# Instanciando a classe Dict
employee_registry = {}

# Inserindo dados
# objeto[chave] = valor
employee_registry[14] = "name1"
employee_registry[23] = "name2"
employee_registry[10] = "name3"
employee_registry[9] = "name4"
print(employee_registry)

# Alterando o nome do id 10
# objeto[chave] = novo_valor
employee_registry[10] = "name30"
print(f"Novo valor do id 10, após a atualização: {employee_registry[10]}")

# Instanciação do objeto vazio
dict1 = {}
dict2 = dict()

# Instanciação com preenchimento inicial de dados
dict3 = {1: "name1", 2: "name2"}
print(f"Dicionário 1: {dict1}")
print(f"Dicionário 2: {dict2}")
print(f"Dicionário 3: {dict3}")

# Inserção e Alteração
# Se a chave não existir no dict, uma nova entrada será criada
# Se já existir, o valor será sobreposto
dict1[14] = "name1"
print(f"Novo dicionário 1, pós inserção/alteração: {dict1}")

# Consulta e Remoção
# Se a chave não existir no dict, causa erro
name = dict1[14]
del dict1[14]
print(f"Dicionário 1 pós consulta e deleção: {dict1}")

"""
Consulte a forma de se criar um dicionário chamada dict comprehension
e crie um dicionário que mapeia inteiros de 3 a 20 para o seu dobro. Exemplo:

- 3 deve ser mapeado para 6;

- 10 deve ser mapeado para 20.
"""

double = {i: i * 2 for i in range(3, 21)}

print(double)

"""
Dada uma string, construa um dicionário com a contagem de cada caractere da
palavra. Utilize o pseudocódigo e o exemplo abaixo para se nortear.

Para cada char na string:
    - Se o char não estiver no dicionário, inclua com o valor 1;

    - Se estiver, incremente o valor.


# Exemplo:

str = "bbbbaaaacccaaaaaaddddddddccccccc"
# saída: {'b': 4, 'a': 10, 'c': 10, 'd': 8}

str = "coxinha"
# saída: {'c': 1, 'o': 1, 'x': 1, 'i': 1, 'n': 1, 'h': 1, 'a': 1}
# Explicação: Nenhuma letra repete em coxinha :)

"""


def count_chars(string):
    count_chars = {}

    for char in string:
        if char not in count_chars:
            count_chars[char] = 1
        else:
            count_chars[char] += 1

    return count_chars


print(count_chars("bbbbaaaacccaaaaaaddddddddccccccc"))


"""
Utilize o dicionário criado no exercício 5. Para as chaves ímpares,
não queremos mais mapear para o seu sobro, mas sim, para o seu triplo.
Consulte o método keys() e atualize o seu dicionário para a nova regra.
"""

double = {i: i * 2 for i in range(3, 21)}

for key in double.keys():
    if key % 2 is not 0:
        double[key] = key * 3

print(double)
