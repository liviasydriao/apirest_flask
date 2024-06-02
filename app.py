from flask import Flask, request, make_response
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, doc='/docs')

user_model = api.model('User',{
    'id':fields.Integer(required = True, description = 'Identificador do usuário'),
    'name':fields.String(required = True, description = 'O nome do usuário'),
    'email':fields.String(required = True, description = 'o e-mail do usuário')
})

users_list = []

user_namespace = api.namespace('users',description = 'operações de usuário')

@user_namespace.route('/<int:user_id>')
class User(Resource):

    @user_namespace.response(200,'Sucess', user_model)
    @user_namespace.response(400,'Not found')

    def get(self,user_id):
        '''Obter o usuário por ID'''
        for user in users_list:
            if 'id' in user and user['id'] == user_id:
                return make_response({'user':user},200)
        return make_response({'msg':'not found'},400)

    @user_namespace.expect(user_model)
    @user_namespace.response(200,'Sucess', user_model)
    @user_namespace.response(400,'Not found')
    def put(self,user_id):
        for idx, user in enumerate(users_list):
            if 'id' in user and user['id'] == user_id:
                users_list[idx] = request.get_json()
                return make_response({'user':users_list[idx]},200)
        return make_response({'msg':'not found'},404)

    @user_namespace.response(200,'Sucess', user_model)
    @user_namespace.response(400,'Not found')
    def delete(self,user_id):
        for idx, user in enumerate(users_list):
            if 'id' in user and user['id'] == user_id:
                deleted = users_list.pop(idx)
                return make_response({'user':deleted},200)
        return make_response({'msg':'not found'},404)


@user_namespace.route('/')
class UserList(Resource):

    @user_namespace.response(200,'Sucess', [user_model])
    
    def get(self):
        return make_response({'users':users_list},200)

    @user_namespace.expect(user_model)
    @user_namespace.response(201,'Created', user_model)
    def post(self):
        new_user = request.get_json()
        users_list.append(new_user)
        return make_response({'user':new_user},201)



if __name__ == '__main__':
    app.run(debug=True)
