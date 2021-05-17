tempo_inicial, tempo_final = input().split(" ")
tempo_inicial = int(tempo_inicial)
tempo_final = int(tempo_final)
if tempo_inicial == tempo_final:
    duracao = 24
else:
    if tempo_inicial > tempo_final:
        duracao = (24 - tempo_inicial) + tempo_final
    else:
        duracao = tempo_final - tempo_inicial
print("O JOGO DUROU {} HORA(S)".format(duracao))