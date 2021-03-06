import pytest

def tabuada(num):
    resposta = []
    for i in range(1, 11):               # i é abreviação de iterator / incremento
        resultado = i * num
        print(f'\n {i} * {num} = {resultado}') # 2
        if i == 1:
            resposta = str(resultado)
        else:
            resposta = resposta + ',' + str(resultado)

    return resposta


def test_tabuada():
    num = 2
    resposta_esperada = '2,4,6,8,10,12,14,16,18,20'
    assert tabuada(num) == resposta_esperada
    print(f'\n Tabuada do {num} \n {resposta_esperada}')

def test_tabuada_vetor():
    num = 2
    resposta_esperada = ['2','4','6','8','10','12','14','16','18','20']
    assert test_tabuada_vetor(num) == resposta_esperada
    print(f'\n Tabuada do {num} \n {resposta_esperada}')