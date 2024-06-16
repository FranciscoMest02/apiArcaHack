'''
Estas son las librerias que instalamos para que funcione la api
pip install flask pymongo
pip install flask-pymongo
pip install flask cors
pip install python-dotenv


Para entrar al ambiente virtual:
venv\Scripts\activate

Este no es el script bueno de la api
'''

#-----------------Esta es la inicializacion de la base de datos-------------------------
#Importamos las librerias
import os
from pickle import TRUE
from dotenv import load_dotenv 
from flask import Flask, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__) #Inicializamos Flask
CORS(app)

#Conectamos con el ID de nuestra base de datos
#app.config['MONGO_URI'] = 'mongodb+srv://' + os.getenv('user') + ':' + os.getenv('password') + '@practicedatabases.n4dtxaz.mongodb.net/laMacara'
#mongo = PyMongo(app) #En esta variable guardamos el acceso a la base de datos


#--------------------------Estas son las llamadas a la base de datos--------------------------------
@app.route('/user/<username>', method=['GET'])
def find_user(username):
    user = mongo.db.users.find_one({'username': username}) #Buscamos en la base de datos, si no encontramos nada retorna None
    if(user == None):
        return {'error': 'Usuario no encontrado'}
    
    return {
        'id': str(user['_id']),
        'username': str(user['username']),
        'nombre': str(user['nombre']),
    }


if __name__ == "__main__":
    app.run(debug=True) #Con el True en debug se reinicia cuando hay cambios