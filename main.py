import random

while True:
    print(20*"-","JOKENPO",20*"-")

    opcoes = ["pedra", "papel", "tesoura"]
    
    traducao = {
        '1': 'pedra',
        '2': 'papel',
        '3': 'tesoura'
    }

    pc = random.choice(opcoes)

    player = input(
        'Qual opção você deseja?\n'
        '[1] Pedra\n'
        '[2] Papel\n'
        '[3] Tesoura\n'
    )

    player = traducao.get(player)

    if player is None:
        print("Opção inválida!\n")
        continue

    print(f"O Player escolheu: {player}")
    print(f"O PC escolheu: {pc}")

    regras = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra"
    }

    if player == pc:
        print('Empate')
    elif regras[player] == pc:
        print('Você venceu!')
    else:
        print('Você perdeu.')
