from flask import Flask, request, Response, jsonify
import requests
from readability import Document

app = Flask(__name__)

@app.route('/read', methods =['GET'])
def read():
    if 'url' in request.args:
        url = request.args['url']
        response = requests.get(url)
        doc = Document(response.text)
        summary = doc.summary()
        title = doc.title()
        data = {
            'title':title,
            'content': summary
            
        }
        return sendresponse(data)
    else:
        return 'url parameter missing'

def sendresponse(data):
    resp = jsonify(data)
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    app.run()