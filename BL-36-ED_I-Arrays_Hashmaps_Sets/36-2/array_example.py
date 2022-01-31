import sys


class Array:
    def __init__(self):
        self.data = []

    def __len__(self):
        # quando pedido o tamanho do array
        # retorne o tamanho de data
        return len(self.data)

    def __str__(self):
        # converte para string e exibe os valores de data
        return str(self.data)

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data.insert(index, value)

    def remove(self, index):
        return self.data.pop(index)

    def update(self, index, value):
        self.data[index] = value


# vamos iniciar e preencher uma estrutura de dados (ED) array
array = Array()

# sys.getsizeof retorna o tamanho da lista em bytes
array_memory_size = sys.getsizeof(array.data)
print(array_memory_size)

array.set(0, "Felipe")
array.set(1, "Ana")
array.set(2, "Shirley")
array.set(3, "Miguel")

# depois de inserir o tamanho é alterado
array_memory_size = sys.getsizeof(array.data)
print(array_memory_size)

array.set(4, "Alberto")
array.set(5, "Marta")
array.set(6, "Túlio")
array.set(7, "Michelle")
array_memory_size = sys.getsizeof(array.data)
print(array_memory_size)

# para acessar um elemento do array, utilizamos seu índice
print(array.get(0))
print(array.get(2))
print("--------")

# removendo um elemento
array.remove(0)

array.update(0, "Joao")

# podemos iterar sobre seus elementos da seguinte maneira
index = 0
# enquanto há elementos no array
while index < len(array):
    # recupere o elemento através do seu índice
    print(f"Index: {index}, Nome: {array.get(index)}")
    index += 1
