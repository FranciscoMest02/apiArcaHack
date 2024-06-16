#-----------------Esta es la inicializacion de la base de datos-------------------------
#Importamos las librerias
import os
from pickle import TRUE
from dotenv import load_dotenv 
from flask import Flask, request
from flask_cors import CORS
from openai import OpenAI
import datetime
import os

import json

app = Flask(__name__) #Inicializamos Flask
CORS(app)

load_dotenv()
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_chatgpt_response(messages):

    list = '''
    - Ciel
    - Del Valle
    - Joya
    - Powerade
    '''


    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "The following message is from a recording. Analyze it and just respond with NOTHING MORE than a json that contains the product type as \"product\" and delivery date as \"date\". If any of those is not present return null in the corresponfing field. For product type, select the best fit from this list: " + list,
            },
            {
                "role": "system",
                "content": "I understand, I will respond with nothing more that the json you asked for.",
            },
            {
                "role": "user",
                "content": messages,
            }
        ],
        model="gpt-3.5-turbo",
    )

    print(response.choices[0].message.content)
    return json.loads(response.choices[0].message.content)

#--------------------------Estas son las llamadas a la base de datos--------------------------------

@app.route('/', methods=["POST"])
def getChatResponse():
    '''return{
        "status": "chat not available"
    }'''
    messages = request.json['messages']
    print(messages)
    model_response = get_chatgpt_response(messages)
    date = datetime.datetime.now()
    model_response.update({'id': date})
    return {"response": model_response}

if __name__ == "__main__":
    app.run(debug=True) #Con el True en debug se reinicia cuando hay cambios