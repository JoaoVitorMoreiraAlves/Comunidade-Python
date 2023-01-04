#--▫️ D E S A F I O  0 1º --
# Crie uma função em Python que receba uma string e retorne um dicionário com as seguintes informações:
# 1) A quantidade de letras (ignorando espaços e caracteres especiais)
# 2) A quantidade de números
# 3) A quantidade de palavras
# 4) A quantidade de vogais

def valida(dic):
    """
    Função com foco em calcular a quantidade de letras, números vogais e palavras que possue na frase, de acordo com o valor dado, ignorando espaços e caracteres especiais! Além disso as palavras só foram consideradas caso aja letras, se for somente números não será considerado uma palavra!
    """
    letra = numero = palavra = vogal = 0
    for i in dic['Frase']:
        for aux in i:
            if aux.isalpha():
                letra += 1
                if aux in 'aáàãâeéèêiíìîoóòôõuúùû':
                    vogal += 1
            elif aux.isnumeric():
                numero += 1
        if i.isalpha():
            palavra += 1

    print(f"A quantidade de letras na frase é de {letra}")
    print(f"A quantidade de número na frase é de {numero}")
    print(f"A quantidade de palavras na frase é de {palavra}")
    print(f"A quantidade de vogais na frase é de {vogal}")


frase = {'Frase':input("Digite a frase: ").split()}
print(f"O dicionário é o seguinte: {frase}")
valida(frase)