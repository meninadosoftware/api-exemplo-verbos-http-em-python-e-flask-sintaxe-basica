
from flask import Flask, request, jsonify
from flask_restful import  Resource, Api
from sqlalchemy import create_engine

db_conect = create_engine('sqlite:///teste.db')
app = Flask(_name_)
api = Api(app)


class Users(Resource):
    def get(self):
        conn = db_conect.conect()
        query = conn.execute("select * from user")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def pos(self):
        conn = db_conect.conect()
        nome = request.json['nome']
        email = request.json['email']
        conn.execute(" insert into values(null, '{0}', '{1}')".format(nome, email))
        query = conn.execute('select * fom user order by id desc limit 1')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self):
        conn = db_conect.conect()
        cod = request.json['cod']
        nome = request.json['nome']
        email = request.json['email']
        conn.execute("update user set nome ='" + str(nome) +
                     "', email ='" + str(email) + "' where cod=%d " % int(cod))
        query = conn.execute("select * from user where cod=%d" % int(cod))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    class UserById(Resource):
        def delete(self, cod):
            conn = db_conect.conect()
            conn.execute("delete from user where cod=%d" % int(cod))
            return {"status ": "success"}

        def get(self, cod):
            conn = db_conect.conect()
            query = conn.execute(" select * from user where cod=%d" % int(cod))
            result = [dict(zip(tuple(query.keys)), i) for i in query.cursor]
            return jsonify(result)


api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<cod>')

if _name_ == '_main_':
    app.run()
