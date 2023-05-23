import requests
import urllib.request as request
import os

def pegar_habilidades(pokemon):
    habilidades_pokemon = []
    for habilidade_pokemon in pokemon['abilities']:
        habilidades_pokemon.append(habilidade_pokemon['ability']['name'])
    return habilidades_pokemon

def pegar_tipo(pokemon):
    tipos_pokemon = []
    tipos_pokemon.append(f'%04d' % pokemon['id'])
    for tipo_pokemon in pokemon['types']:
        tipos_pokemon.append(tipo_pokemon['type']['name'])
    return tipos_pokemon

def pegar_nome(pokemon):
    nome_pokemon = pokemon['name']
    return nome_pokemon

def pega_status(pokemon):
    status_pokemon = {}
    for stat_pokemon in pokemon['stats']:
        status_pokemon[stat_pokemon['stat']['name']] = stat_pokemon['base_stat']
    return status_pokemon

def pega_imagem(pokemon):
    pasta = '.\\imagens\\imagens_pokemon'
    for imagem in os.listdir(pasta):
        os.remove(os.path.join(pasta, imagem))
    imagem = pokemon['sprites']['other']['official-artwork']['front_default']
    request.urlretrieve(imagem,f'imagens\imagens_pokemon\{nome_pokemon}.png')

def main(i):
    global nome_pokemon
    nome_pokemon = i
    api = f'https://pokeapi.co/api/v2/pokemon/{nome_pokemon}'
    res = requests.get(api)

    if res.status_code == 200:
        pokemon = res.json()
        habilidades = pegar_habilidades(pokemon)
        tipo = pegar_tipo(pokemon)
        status = pega_status(pokemon)
        informacoes = pegar_nome(pokemon)
        pega_imagem(pokemon)

        pokemon_dados = {}
        
        pokemon_dados[f'{informacoes}'] = {
            'status': status,
            'habilidades': habilidades,
            'tipo': tipo
        }

        return pokemon_dados

def pokemon_inicial(i):
    global nome_pokemon
    nome_pokemon = i
    api = f'https://pokeapi.co/api/v2/pokemon/bulbasaur'
    res = requests.get(api)
    if res.status_code == 200:
        pokemon = res.json()

        habilidades = pegar_habilidades(pokemon)
        tipo = pegar_tipo(pokemon)
        status = pega_status(pokemon)
        informacoes = pegar_nome(pokemon)
        pega_imagem(pokemon)

        pokemon_dados = {}
        
        pokemon_dados[f'{informacoes}'] = {
            'status': status,
            'habilidades': habilidades,
            'tipo': tipo
        }
    
        return pokemon_dados
