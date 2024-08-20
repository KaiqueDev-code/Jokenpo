import random
# escolhi a linguagem Python
#Trabalho feito por: Kaique Santana De Almeida
#serve para o usuario fazer sua escolha
def escolha_usuario():
    opcao = input("Escolha uma das opções: pedra, papel ou tesoura: ").lower()
    while opcao not in ["pedra", "papel", "tesoura"]:
        opcao = input("Opção inválida! Escolha uma: pedra, papel, tesoura: ").lower()
    return opcao

def escolha_maquina():
    return random.choice(["pedra", "papel", "tesoura"])
#cerebro do codigo, definição das regras
def quem_venceu(escolha_usuario, escolha_maquina):
    if escolha_maquina == escolha_usuario:
        return "empate"
    elif (escolha_usuario == "pedra" and escolha_maquina == "tesoura") or \
         (escolha_usuario == "papel" and escolha_maquina == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_maquina == "papel"):
        return "usuario"
    else:
        return "maquina"
#O placar
def placar(placar_maquina, placar_usuario):
    print(f"Placar: Máquina {placar_maquina} x {placar_usuario} Usuário")

# serve para o que o usuario escolha numeros ao inves de letras
def pedir_vezes_jogadas():
    while True:
        try:
            vezes_jogadas = int(input("Quantas vezes você quer jogar? "))
            if vezes_jogadas > 0:
                return vezes_jogadas
            else:
                print("Por favor, insira um número maior que zero.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

def jogar_novamente():
    placar_maquina = 0
    placar_usuario = 0
    vezes_jogadas = int(input("Quantas vezes você quer jogar? "))

   

    for _ in range(vezes_jogadas):
        escolha_pc = escolha_maquina()
        escolha_user = escolha_usuario()
        print(f"Você escolheu {escolha_user}, e o computador escolheu {escolha_pc}.")

        vencedor = quem_venceu(escolha_user, escolha_pc)

        if vencedor == "usuario":
            print("Você venceu esta rodada!")
            placar_usuario += 1
        elif vencedor == "maquina":
            print("A máquina venceu esta rodada!")
            placar_maquina += 1
        else:
            print("Esta rodada foi um empate!")

        placar(placar_maquina, placar_usuario)
#repetição pro usuario jogar quantas vezes quiser
while True:
    jogar_novamente()
    resposta = input("Você quer jogar novamente? (s/n): ").lower()
    if resposta != 's':
        print("Obrigado por jogar!")
        break
