# 1 - imports
import json

import pytest
import csv
import requests

test_advice = [
    (1, 'Advice', 'Don t give to others advice which you wouldn t follow.'),  # advice 1
    (2, 'Advice', 'Don t take life too seriously.')  # advice 2
]


# teste_dados_novos_produtos = [
#  (1, 'Gucci', 'Marmont', 'R$ 6.000,00'),       # bolsa 1
# (2, 'Dior', 'Lady','R$ 10.000,00')            # bolsa 2

@pytest.mark.parametrize('id,advice')
def test_advice(id, advice):  # função que testa o algo
    try:
        response = requests.get(f'https://api.adviceslip.com/advice/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        advice_obtido = jsonResponse['data']['advice']

        print(f'id: {id_obtido} \n - advice: {advice_obtido} \n ')
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == id
        assert advice_obtido == advice

    except HTTPError as http_fail:  # Para o ISTQB, descobriu rodando é falha
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:  # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada: {fail}')


# função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users/{id}

# Leitor do Arquivo CSV
def ler_dados_do_csv():
    test_rick_csv = []
    nome_arquivo = 'lista07.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            next(dados)
            for linha in dados:
                test_rick_csv.append(linha)
        return test_rick_csv
    except FileNotFoundError:
        print(f'Deu ruinzão: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {nome_arquivo}')


@pytest.mark.parametrize('id,name,status,species,type,gender,origin', ler_dados_do_csv())
def test_rick_csv(id, name, status, species, type, gender, origin):  # função que testa o algo
    try:
        response = requests.get(f'https://rickandmortyapi.com/api/character/485{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        name_obtido = jsonResponse['data']['name']
        status_obtido = jsonResponse['data']['status']
        species_obtido = jsonResponse['data']['species']
        type_obtido = jsonResponse['data']['type']
        gender_obtido = jsonResponse['data']['gender']
        origin_obtido = jsonResponse['data']['origin']

        print(
            f'id: {id_obtido} \n name: {name_obtido} \n status: {status_obtido} \n species: {species_obtido} \n type: {type_obtido} \n gender: {gender_obtido} \n origin: {origin_obtido} \n')
        print(json.dumps(jsonResponse, indent=2, sort_keys=True))

        assert id_obtido == id
        assert name_obtido == name
        assert status_obtido == status
        assert species_obtido == species
        assert type_obtido == type
        assert gender_obtido == gender
        assert origin_obtido == origin

    except HTTPError as http_fail:  # Para o ISTQB, descobriu rodando é falha
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:  # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada: {fail}')
