# 1 - imports - bibliotecas
import pytest
# 2 - class - classe

# 3 - definitions - definições = métodos e funções
def print_hi(name):
    print(f'Oi, {name}')

#oi

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 / numero2 # bug!!

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return 'Não dividirás por zero'

# Testes Unitarios / Teste de Unidades

 # teste da função de somar
def test_somar_didatico():
    # 1 - Configura / Prepara
    numero1 = 8 # input / entrada
    numero2 = 5 # input / entrada
    resultado_esperado = 13 # output / saida
    # 2 - Executa
    resultado_atual = somar(numero1,numero2)
    # 3 - Check / Valida
    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('numero1,numero2,resultado',[
    #valores
    (5, 4, 9), # teste 1
    (3, 2, 5), # teste 2
    (10,6, 16), # teste 3
])
def test_somar(numero1, numero2, resultado):
    assert somar(numero1,numero2) == resultado

def test_somar_resultado_negativo():
    assert somar(-1000,-2000) == -3000

def test_subtrair():
    assert subtrair(4,5) == -1

def test_multiplicar():
    assert multiprlicar(3,7) == 21

def test_dividir():
    assert dividir(8,4) == 2

# Dia 1 : 100 testes : 0 passaram
# Dia 2 : 100 testes : 5 passaram
# Dia 3 : 100 testes : 15 passaram
# Dia 4 : 100 testes : 30 passaram

#TDD : Desenvolvimento Direcionado pelo Testes
# - Criar o esqueleto de classes, funções e métodos logo no início da Sprint
# - Criar pelo 1 teste (feliz) para todas as funções e métodos
# - Executar todos os testes unitários diariamente para medir o progresso


if __name__ == '__main__':
    print_hi('Jose')

    # soma de 2 números
    resultado = somar(4,2)
    print(f'O resultado da soma: {resultado}')

    # subtração de 2 números
    resultado = subtrair(5,3)
    print(f'O resultado da subtração: {resultado}')

    # multiplicação
    resultado = multiplicar(2,4)
    print(f'O resultado da multiplicação: {resultado}')

    # divisão
    resultado = dividir(9,8)
    print(f'O resultado da divisão: {resultado}')

