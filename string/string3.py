#Python usa o símbolo de adição (+) para combinar strings.

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

'''
Nesse exemplo, usamos + para criar um nome completo combinando
first_name, um espaço e last_name u, o que resultou em: ada lovelace
Esse método de combinar strings se chama concatenação. 

'''
'''
Podemos usar concatenação para compor uma mensagem e então
armazenar a mensagem completa em uma variável:
'''
first_name ="ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + "!"

print(message)

'''
Esse código exibe a mensagem “Hello, Ada
Lovelace!”, mas armazenar a mensagem em uma variável deixa a
instrução print final  muito mais simples.

'''