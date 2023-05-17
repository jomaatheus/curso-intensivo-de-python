'''
Uma string é simplesmente uma série de caracteres. Tudo que estiver
entre aspas é considerada uma string em Python, e você pode usar aspas
simples ou duplas em torno de suas strings, assim: "This is a string."
'This is also a string.'
Essa flexibilidade permite usar aspas e apóstrofos em suas strings: 'I
told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
'''

name='ada lovelace'

print(name.title())
#title() exibe cada palavra com uma letra maiúscula no início.
print(name.upper())
#você pode mudar uma string para que tenha somente letras maiúsculas
print(name.lower())
#você pode mudar uma string para que tenha somente letras minusculas

'''
Um método é uma ação que Python pode executar em um dado. O ponto (.) após name em
name.title() informa a Python que o método title() deve atuar na variável
name. Todo método é seguido de um conjunto de parênteses, pois os
métodos, com frequência, precisam de informações adicionais para realizar
sua tarefa. Essas informações são fornecidas entre os parênteses. A
função title() não precisa de nenhuma informação adicional, portanto seus
parênteses estão vazios.

'''