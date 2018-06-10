import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from .resources.item import Item, Items
from .resources.store import Store, Stores
from .resources.user import UserRegister, User
from .security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'nerijus'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
