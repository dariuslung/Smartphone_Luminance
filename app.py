from flask import Flask, request, abort, escape
from flask import render_template
from flask import make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def page():
    return make_response(render_template('index.html'))

if __name__ == '__main__':
    app.run(ssl_context=('server.crt', 'server.key'), host='0.0.0.0', port=443, threaded=True, use_reloader=False)