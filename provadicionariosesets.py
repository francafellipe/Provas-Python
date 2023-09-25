#Crie uma função chamada maior_idade que recebe um dicionário como argumento e retorna o nome da pessoa com a maior idade.
pessoas = {"João": 23,"Maria": 28,"Pedro": 35,"Lucas": 19}

def maior_idade(pessoas):
    maior_idade = 0
    pessoa_mais_velha = ""
    for nome, idade in pessoas.items():
        if idade > maior_idade:
            maior_idade = idade
            pessoa_mais_velha = nome
    return pessoa_mais_velha

# acesse a idade da pessoa joao e armazene em uma variavel idade_joao
pessoas = {"João": 23,"Maria": 28,"Pedro": 35,"Lucas": 19}

idade_joao = pessoas["João"]

print(idade_joao)
# adicione uma pessoa ao dicionario com nome ana e idade 31
pessoas["Ana"]= 31

print(pessoas)


print(maior_idade(pessoas))

