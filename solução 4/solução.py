string = input("Digite uma string: ")
tamanho = len(string)
string_invertida = ""

for i in range(tamanho):
    string_invertida += string[tamanho - i - 1]

print("String original:", string)
print("String invertida:", string_invertida)
