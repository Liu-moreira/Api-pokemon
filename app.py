from flask import Flask
from service import Service
import json

app = Flask(__name__)

@app.route('/obterPokemon/<p_nome>', methods=['GET'])
def obterPokemon(p_nome):  
    service = Service()
    pokemons = service.obterPokemons()
    for pokemon in pokemons['results']:
        if pokemon['name'] == p_nome:
            return pokemon
    return "Erro: Pokemon não encontrado"
 


@app.route('/listarPokemons', methods=['GET'])
def listarPokemons():  
    service = Service()
    pokemons = service.obterPokemons()
    poke_names = [dict(name = k1['name']) for k1 in pokemons['results']]
    resultado = json.dumps(poke_names)
    return resultado
    return json.dumps(poke_names) 