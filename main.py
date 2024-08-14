# Tupla de chaves
chaves = ('Nome', 'Idade', 'Profissão')

# Lista de dicionários
usuarios = [
    {
        chaves[0]: 'Fulano',
        chaves[1]: '20',
        chaves[2]: 'Programador'
    },
    {
        chaves[0]: 'Fulane',
        chaves[1]: '24',
        chaves[2]: 'Presidente'
    },
    {
        chaves[0]: 'Fulana',
        chaves[1]: '26',
        chaves[2]: 'Sanitário ambulante.'
    }
]

# Mostrar a lista de usuários
print(f'{"="*10} LISTA DE USUÁRIOS {"="*10}\n')

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
    print(f'\n{"-"*10}\n')

# Adicionar novo dicionário à lista
novo_usuario = {}
for chave in chaves:
    valor = input(f'Informe {chave}: ')
    novo_usuario[chave] = valor

usuarios.append(novo_usuario)

print(f'\n{"="*10} LISTA DE USUÁRIOS {"="*10}\n')

# Mostrar a lista de usuários novamente com o novo usuário
for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
    print(f'\n{"-"*10}\n')
