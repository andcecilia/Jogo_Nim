print("Bem-vindo ao jogo do NIM! Escolha:")

def partida_ou_campeonato():
    umoudois = ""
    while umoudois != "1" and umoudois!= "2":
        umoudois = input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato ")
        if umoudois != "1" and umoudois != "2":
            print("Você deve digitar 1 ou 2 para escolher")
    if umoudois == "1":
        partida()
    if umoudois == "2":
        campeonato()

def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    vezDoPC = False

    if n % (m+1) == 0:
        print("Você começa!")
    else:
        print("Computador começa!")
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            peças_pc = computador_escolhe_jogada(m, n)
            n = n - peças_pc
            if peças_pc == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", peças_pc, "peças.")
            vezDoPC = False
        else:
            peças_user = usuario_escolhe_jogada(m,n)
            n = n - peças_user
            if peças_user == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", peças_user, "peças.")
            vezDoPC = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            if n != 0:
                print("Agora restam", n, "peças no tabuleiro.")
    print("Fim do jogo! O computador ganhou!")

def usuario_escolhe_jogada(m,n): #exemplo, n=totalpeças=6 e m=limite peças=2
    jogadaValida = False
    while not jogadaValida:
        peças_user = int(input("Quantas peças você vai tirar?"))
        if peças_user > m or peças_user < 1:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            jogadaValida = True
    return peças_user

def computador_escolhe_jogada(m,n):
    peças_pc = 1
    while peças_pc != m:
        if (n-peças_pc) % (m+1) == 0:
            return peças_pc
        else:
            peças_pc +=1
    return peças_pc

def campeonato():
    print("Você escolheu um campeonato!")
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 x 3 Computador)")

partida_ou_campeonato()