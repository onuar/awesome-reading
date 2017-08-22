import requests
from werkzeug.wrappers import Request, Response
from readability import Document

port = 5200


@Request.application
def application(request):
    if str(request.path) == '/favicon.ico':
        return None

    print(request.path)

    r_response = requests.get(request.args.get("read"))
    doc = Document(r_response.text)

    response = Response(doc.summary(), status=200, content_type="text/html; charset=utf-8")
    return response


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', port, application, use_reloader=True, threaded=True)
