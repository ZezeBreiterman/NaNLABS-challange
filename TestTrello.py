import requests
import json
import random
import flask


key = "2ee6fda76a7708c981959fb6219fe71f"
token = "88172b6a2658ef853b039cf5d326afcddee17f0a728d483158de189b3b36d896"
WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "anticipation")

def addIssue(title, description):


    url = "https://api.trello.com/1/cards"
    query = {
    'key': key,
    'token': token,
    'idList': '60b28a97b5c9b872e3be50c5',
    'name': title,
    'desc': description
    }
    response = requests.request(
    "POST",
    url,
    params=query
    )
def addBug(description):

    url = "https://api.trello.com/1/cards"

    
    randWord = random.choice(WORDS)
    randNumb = str(random.randint(100, 999))

    query = {
    'key': key,
    'token': token,
    'idList': '60b28a97b5c9b872e3be50c5',
    'idMembers': getRandomMember(),
            #bug-{word}-{number}
    'name': ('bug-' + randWord + '-' + randNumb),
    'desc': description,
    'idLabels': '60b3f75978e9a579fe70c8de'
    }
    response = requests.request(
    "POST",
    url,
    params=query
    )  
def AddTask(title,category):
    if category.lower() == 'maintenance':
     label = '60b3f9d9b40fae8fab64e3c7'
    if category.lower() == 'research':
     label = '60b3f9f638a7000bcfd0ef06'
    if category.lower() == 'test':
     label = '60b3fa040247d138d947f9cc'
    if (category.lower() != 'test') and (category.lower() != 'research') and (category.lower() != 'maintenance'):
     label = '60b3fef1f692c4109a94bc73'
    

    url = "https://api.trello.com/1/cards"

    query = {
    'key': key,
    'token': token,
    'idList': '60b28a97b5c9b872e3be50c6',
    'name': title,
    'idLabels': label
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )
def getRandomMember():
    url = "https://api.trello.com/1/boards/60b28a97b5c9b872e3be50c4/members"

    response = requests.request(
       "GET",
       url
    )
    idsNoSorted = response.json()
    ids = []
    for item in idsNoSorted:
        id = item.get("id")
        ids.append(id)

    return(random.choice(ids))

from flask import Flask
from flask import request, jsonify


app = Flask(__name__)
@app.route("/",methods = ['POST'])
def home():
    body = request.get_json()
    type = body.get("type")
    print(body)
    if type =='issue':
        title = body.get("title")
        description = body.get("description")
        addIssue(title, description)
    elif  type == 'bug':
        description = body.get("description")
        addBug(description)
    elif  type == 'task':
        description = body.get("title")
        category = body.get("category")
        AddTask(description, category)
    return jsonify({"status": "ok"})


    

if __name__=="__main__":
    app.run()    
    

    
# addIssue("no anda algo","Probando descripcion")
#addBug('test1 Description')
# addBug('test2 Description')
# addBug('test2 Description')
#AddTask('titulo 2', 'Maintenance')
# AddTask('titulo 2', 'Research')
# AddTask('titulo 3', 'test')
# AddTask('titulo 4', 'asd')

