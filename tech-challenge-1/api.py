from flask import Flask, request, Response
from flask_restx import Resource, Api
import pandas as pd

# Cria um app Flask com nome do arquivo atual
app = Flask(__name__)
api = Api(app,
          version='1.0',
          default='Dados de produção e comercialização de vinhos',
          default_label='',
          title='Api para consulta de dados da Embrapa',
          description='Api para consulta de dados da Embrapa',
          doc='/docs')

#dados_producao = pd.read_csv('dados/Producao.csv', sep=';')
#dados_processamento = pd.read_csv('dados/ProcessaViniferas.csv', sep='\t')
#dados_comercializacao = pd.read_csv('dados/Comercio.csv', sep=';')
#dados_importacao = pd.read_csv('dados/ImpVinhos.csv', sep=';')
#dados_exportacao = pd.read_csv('dados/ExpVinho.csv', sep=';')

dados_producao = pd.read_csv('http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv', sep=';')
dados_processamento = pd.read_csv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv', sep=';')
dados_comercializacao = pd.read_csv('http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv', sep=';')
dados_importacao = pd.read_csv('http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv', sep=';')
dados_exportacao = pd.read_csv('http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv', sep=';')

# Padroniza nomes das colunas e limpa alguns espaços em branco
dados_importacao.rename(columns={'Id':'id'}, inplace=True)
dados_exportacao.rename(columns={'Id':'id'}, inplace=True)

colunas = dados_producao.columns.to_list().copy()
colunas.insert(1,'categoria')

dados_comercializacao = dados_comercializacao.set_axis(colunas, axis=1)
dados_comercializacao['produto'] = dados_comercializacao['produto'].str.strip()


# Métodos reutilizados nos serviços rest
def list_all(df):
    return Response(df.to_json(index=True,orient="records"), mimetype='application/json')


def find_by_id(df, id):
    retorno = df[df.id == id]
    return Response(retorno.to_json(orient="records"), mimetype='application/json')


# ----------------- Dados de produção -----------------

@api.route('/producao')
class ProducaoRest(Resource):

    @api.doc(description='Lista de todos os registros de produção de vinhos')
    def get(self):
        return list_all(dados_producao)


# ----------------- Dados de processamento -----------------
    
@api.route('/processamento')
class ProcessamentoRest(Resource):

    @api.doc(description='Lista de todos os registros de processamentos')
    def get(self):
        return list_all(dados_processamento)


# ----------------- Dados de comercialização -----------------

@api.route('/comercializacao')
class ProcessamentoRest(Resource):

    @api.doc(description='Lista de todos os registros de comercialização')
    def get(self):
        return list_all(dados_comercializacao)


# ----------------- Dados de importação -----------------

@api.route('/importacao')
class ProcessamentoRest(Resource):

    @api.doc(description='Lista de todos os registros de importação')
    def get(self):
        return list_all(dados_importacao)


# ----------------- Dados de exportação -----------------

@api.route('/exportacao')
class ProcessamentoRest(Resource):

    @api.doc(description='Lista de todos os registros de exportação')
    def get(self):
        return list_all(dados_exportacao)


# Start do serviço na porta 5000
app.run(port= 5000, host='localhost', debug=True)