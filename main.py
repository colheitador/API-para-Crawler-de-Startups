# função para que a API peça uma cidade ou sigla de estado para pesquisar

# pacotes
from fastapi import FastAPI, HTTPException # para trabalhar com a API
import sqlite3
import json

# nome para chamar o FastAPI
app = FastAPI()

# para conexão com o banco de dados
con3 = sqlite3.connect("./startups.db", check_same_thread=False)
cursor3 = con3.cursor()

@app.get("/startups/cidade_ou_sigla_do_estado")
def pesquisar_por_cidade_ou_sigla_do_estado(cidade_ou_estado: str):
    # para isso, vamos criar um filtro para que apenas a localidade desejada seja mostrada	
	selecionar_localidade_buscada = f"SELECT * FROM tab_startups_3 WHERE cidade_c LIKE ('%{cidade_ou_estado.upper()}%') " #### ?", (f'%{cidade_ou_estado.upper()}%',)
	cursor3.execute(selecionar_localidade_buscada)   ##, ((cidade_ou_estado.upper()),))
	informacoes_sobre_startups = cursor3.fetchall()
	resultados = [] ## os resultados (em forma de dicionarios) serao adicionados a essa lista
	for cada_linha_tabela_de_startups in informacoes_sobre_startups:
		cada_dicionario_de_startups = {
			"Nome da startup": cada_linha_tabela_de_startups[0],
            "Cidade": cada_linha_tabela_de_startups[1],
            "Frase": cada_linha_tabela_de_startups[2],
            "Mercado": cada_linha_tabela_de_startups[3],
            "Publico-alvo": cada_linha_tabela_de_startups[4],
            "Modelo de receita": cada_linha_tabela_de_startups[5],
            "Momento": cada_linha_tabela_de_startups[6],
            "Sobre": cada_linha_tabela_de_startups[7],
            "Localizacao": cada_linha_tabela_de_startups[8],
            "Url curta": cada_linha_tabela_de_startups[9],
            "Segmento secundario": cada_linha_tabela_de_startups[10],
            "Fundacao": cada_linha_tabela_de_startups[11],
            "Tamanho do time": cada_linha_tabela_de_startups[12],
            "Atualizacao": cada_linha_tabela_de_startups[13],
            "Redes sociais": cada_linha_tabela_de_startups[14],
            "Visite o site": cada_linha_tabela_de_startups[15],
            "Principais integrantes": cada_linha_tabela_de_startups[16],
            "Outros integrantes": cada_linha_tabela_de_startups[17]
            }
        # agora adicionar os dicionários (com conteúdo de startups) a uma lista para mostrar na tela
		resultados.append(cada_dicionario_de_startups)
        #print(cada_linha_tabela_de_startups)
        #resultados.append(cada_linha_tabela_de_startups)
	numero_de_resultados = "Foram encontrados " + str(len(resultados)) + " resultados para esta busca: " + cidade_ou_estado

	return resultados # caso queira mostrar os resultados da busca em .json, comente esta linha e descomente a "return json.dumps(resultados)"
	#return numero_de_resultados, json.dumps(resultados) # caso Não queira mostrar os resultados da busca em .json, comente esta linha e  descomente a "return resultados"