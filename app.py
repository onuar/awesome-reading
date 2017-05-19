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

        data = {
            'content': summary
        }
        resp = jsonify(data)
        resp.status_code = 200
        return resp
    else:
        return 'url parameter missing'

if __name__ == '__main__':
    app.run()