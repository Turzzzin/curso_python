fruits = ['abacate', 'abacaxi', 'banana', 'morango', 'kiwi']

"""for item in fruits:
    if 'b' in item:
        fruits2.append(item)"""

fruits2 = [item for item in fruits if 'b' in item]

print(fruits2)