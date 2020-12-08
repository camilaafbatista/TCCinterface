from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
from json2html import *
from models import Contrato, Disciplina, Atribuicao, db_session

app = Flask(__name__)
api = Api(app)


class Contratos(Resource):
    def get(self):
        contrato = db_session.query(Contrato).distinct(
            Contrato.contrato).group_by(Contrato.contrato)
        response = [{
            'contrato': i.contrato,
            'horas_habeis': i.horas_habeis,
        } for i in contrato]
        table = json2html.convert(json=response)
        headers = {'Content-Type': 'text/html'}
        return make_response(
            render_template("home.html", table=table), headers)

    def post(self):
        contrato = db_session.query(Contrato).distinct(
            Contrato.contrato).group_by(Contrato.contrato)
        response = [{
            'contrato': i.contrato,
            'horas_habeis': i.horas_habeis,
        } for i in contrato]
        table = json2html.convert(json=response)
        headers = {'Content-Type': 'text/html'}
        return make_response(
            render_template("search.html", table=table), headers)


class Visualizar(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("visualizar.html"), headers)


class Disciplinas(Resource):
    def get(self, cod_jupiter):
        cod_jupiter = db_session.query(Disciplina).filter_by(
            cod_jupiter=cod_jupiter)
        response = [{'contrato': i.contrato} for i in cod_jupiter]
        return response


class Atribuicoes(Resource):
    def get(self):
        cod_jupiter = db_session.query(Atribuicao).all()
        response = [{
            'contrato': i.contrato,
            'cod_jupiter': i.cod_jupiter,
            'disciplina': i.disciplina
        } for i in cod_jupiter]
        return response

    def post(self):
        dados = request.json
        atribuicoes = Atribuicao(
            contrato=dados['contrato'],
            cod_jupiter=dados['cod_jupiter'],
            disciplina=dados['disciplina'])
        atribuicoes.save()
        response = {
            'contrato': atribuicoes.contrato,
            'cod_jupiter': atribuicoes.cod_jupiter,
            'disciplina': atribuicoes.disciplina
        }
        return response


api.add_resource(Contratos, '/')
api.add_resource(Visualizar, '/visualizacao')
api.add_resource(Disciplinas, '/<string:cod_jupiter>')
api.add_resource(Atribuicoes, '/atribuicoes')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
