import random


MAX_LINHAS = 3
MAX_APOSTA = 100
MIN_APOSTA = 1

FILEIRAS = 3
COLUNAS = 3

quantidade_de_icones = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

valores_dos_icones = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def verifica_os_ganhos(colunas, linhas, aposta, valores):
    ganhos = 0
    linhas_ganhas = []

    for linha in range(linhas):
        icone = colunas[0][linha]

        for coluna in colunas:
            icone_para_checar = coluna[linha]
            if icone != icone_para_checar:
                break
        else:
            ganhos += valores[icone] * aposta
            linhas_ganhas.append((linha + 1))

    return ganhos, linhas_ganhas


def verifica_digito(numero):
    while True:
        if numero.isdigit():
            numero = int(numero)
            break
        else:
            numero = input("Por favor digite um número: ")

    return numero


def pega_caca_niquel_icones(fileiras, colunas, icones):
    todos_os_icones = []

    # Para cada ícone e sua quantidade especificada no dicionário 'icones'
    for icone, quantidade_dos_icones in icones.items():

        # Adiciona a quantidade especificada desse ícone à lista 'todos_os_icones'
        for _ in range(quantidade_dos_icones):
            todos_os_icones.append(icone)

    colunas_do_jogo = []

    for _ in range(colunas):
        coluna = []
        icones_atuais = todos_os_icones[:]  # Faz uma cópia da lista 'todos_os_icones' para as próximas operações

        for _ in range(fileiras):
            valor = random.choice(icones_atuais)
            icones_atuais.remove(valor)
            coluna.append(valor)

        colunas_do_jogo.append(coluna)

    return colunas_do_jogo


"""
A função enumerate retorna um iterador que gera tuplas contendo dois elementos em cada iteração:

O primeiro elemento é o índice (posição) do item na sequência.
O segundo elemento é o próprio item da sequência.
"""


def imprima_caca_niquel(colunas):
    for fileira in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):  # O i representa o índice da coluna e "coluna" representa a lista coluna.
            if i != len(colunas) - 1:  # Verifica se o indice não está no final da coluna
                print(coluna[fileira], end=" | ")
            else:
                print(coluna[fileira], end="")

        print()


def deposito():
    while True:
        quantia = input("Quanto você gostaria de depositar? $")
        quantia = verifica_digito(quantia)
        if quantia > 0:
            break
        else:
            print("A quantia deve ser maior que 0.")

    return quantia


def pergunta_numero_de_linha():
    while True:
        linhas = input(f"Digite o número de linhas para apostar (1-{MAX_LINHAS}): ")
        linhas = verifica_digito(linhas)
        if 1 <= linhas <= MAX_LINHAS:
            break
        else:
            print("Digite um número válido de linhas.")

    return linhas


def pergunta_aposta():
    while True:
        quantia_por_linha = input("Quanto você gostaria de apostar em cada linha? $")
        quantia_por_linha = verifica_digito(quantia_por_linha)
        if MIN_APOSTA <= quantia_por_linha <= MAX_APOSTA:
            break
        else:
            print(f"A quantia da aposta deve ser entre ${MIN_APOSTA} - ${MAX_APOSTA}. ")

    return quantia_por_linha


def giro(saldo):
    linhas = pergunta_numero_de_linha()

    while True:
        aposta_por_linha = pergunta_aposta()
        aposta_total = aposta_por_linha * linhas

        if aposta_total > saldo:
            print(f"Você não tem saldo o sufuciente para apostar essa quantia. Seu saldo atual é de ${saldo}.")
        else:
            break

    print(f"Você está apostando ${aposta_por_linha} em {linhas} linhas. O total da aposta é igual a ${aposta_total}.")
    caca_niquel = pega_caca_niquel_icones(FILEIRAS, COLUNAS, quantidade_de_icones)
    imprima_caca_niquel(caca_niquel)
    ganhos, linhas_ganhas = verifica_os_ganhos(caca_niquel, linhas, aposta_por_linha, valores_dos_icones)
    print(f"Você ganhou ${ganhos}!")
    print("Você ganhou nas linhas:", *linhas_ganhas)

    return ganhos - aposta_total


def main():
    saldo = deposito()
    while True:
        print(f"Saldo atual é de ${saldo}.")
        resposta = input("Pressione enter para jogar ou digite 'sair' para sair. ")
        while resposta not in ["sair", ""]:
            resposta = input("Entrada inválida. Pressione Enter para jogar ou digite 'sair' para sair: ")
        if resposta == "sair":
            break
        else:
            saldo += giro(saldo)

    print(f"Você ficou com ${saldo}")


if __name__ == "__main__":
    main()
