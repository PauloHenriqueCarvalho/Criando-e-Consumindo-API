import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def homepage():
    return 'HomePage'

@app.route('/alunos')
def alunos():
    tabela = pd.read_csv('base_dados.csv')
    dados = tabela.to_dict(orient='records')  # Converte cada linha em um dicionário
    return jsonify(dados)

app.run(host='0.0.0.0')



# tabela = pd.read_csv('advertising.csv')
# total_vendas = tabela['Vendas'].sum()
# print(total_vendas)