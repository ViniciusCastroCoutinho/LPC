import random

CHANCE = 5
letras = 'abcdefghijk lmnopqrstuvwxyz'
frase = ''
WEASEL = 'methinks it is like a weasel'
score = 0
geração = 0

for i in range(28):
    frase += letras[random.randint(0, 26)]

print(frase)


def update():
    global frase, WEASEL, score, CHANCE
    for i in range(100):
        novo_score = 0
        nova_frase = list(frase)
        for c in range(28):
            if random.randint(0, 99) < CHANCE:
                nova_frase[c] = letras[random.randint(0, 26)]
        for i in range(28):
            if nova_frase[i] == list(WEASEL)[i]:
                novo_score += 1
        if novo_score > score:
            score = novo_score
            frase = ''
            for i in range(28):
                frase += nova_frase[i]
while score != 28:
    update()
    geração += 1
    print(f'Geração {geração}: ' + frase)
        