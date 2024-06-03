# Challenges #

'''
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

# def fizzbuzz(n):
#     for i in range(1, n+1):
#         divisibleByThree = i % 3 == 0
#         disibleByFive = i % 5 == 0
#         if divisibleByThree and disibleByFive:
#             print("FIZZBUZZ")
#         elif divisibleByThree:
#             print("FIZZ")
#         elif disibleByFive:
#             print("BUZZ")
#         else:
#             print(i)

# fizzbuzz(100)

'''
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
''' 

word_one = "Amorss"
word_two = "maorss"

def is_anagram(word_one: str, word_two: str) -> bool:
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram(word_one, word_two))