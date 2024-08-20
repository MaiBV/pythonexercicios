import requests


def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/01001000/json/')
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return


def retorna_dados_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    response = retorna_response('https://globallabs.academy/')
    print(response)
    #retorna_dados_cep('22041001')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon)