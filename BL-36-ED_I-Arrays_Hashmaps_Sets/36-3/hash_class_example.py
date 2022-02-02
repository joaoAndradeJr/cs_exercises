class Employee:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name


"""
Considerando que nossa chave são inteiros, vamos usar a operação mod 10 , ou
resto da divisão inteira por 10, para definirmos o índice onde o dado vai ser
armazenado. Cada número que entra, vai resultar em um endereço de 0 a 9. O
valor 10 foi escolhido por não ser muito grande. Tanto a operação mod como o
valor 10 são escolhas ilustrativas e são apenas um exemplo.
Vamos inicializar nossa classe HashMap e definir o método get_address() :
"""


class HashMap:
    def __init__(self):
        self._buckets = [[] for i in range(10)]

    def get_address(self, id_num):
        return id_num % 10

    """
    Para povoar nossa hash, recebemos o objeto, computamos o seu address, a
    partir da chave numérica, e armazenamos no local adequado.
    """

    def insert(self, employee):
        address = self.get_address(employee.id_num)
        self._buckets[address].append(employee)

    """
    Para acessar o dado de interesse, passamos a chave. A classe identifica o
    índice, onde a referência para aquele objeto está armazenada, e retorna o
    valor que estiver no campo name
    """

    def get_value(self, id_num):
        address = self.get_address(id_num)

        for item in self._buckets[address]:
            if item.id_num == id_num:
                return item.name
        return None

    """
    Para consultar se uma determinada chave existe dentro da sua hash map,
    basta calcular o address . Além disso, vamos certificar de que o conteúdo
    da lista buckets não é None.
    """

    def has(self, id_num):
        address = self.get_address(id_num)
        return self._buckets[address] is not None

    def update(self, id_num, new_name):
        address = self.get_address(id_num)

        # for item in self._buckets[address]:

        employee = self._buckets[address]
        employee.name = new_name


employees = [(14, "name1"), (23, "name2"), (10, "name3"), (9, "name4")]
registry = HashMap()

for id_num, name in employees:
    employee = Employee(id_num, name)
    registry.insert(employee)

print(registry.get_value(10))

registry.update(10, "João")

print(registry.get_value(10))
