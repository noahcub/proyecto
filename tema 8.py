from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Mi primer programa Flask!'

if __name__ == '__main__':
    app.run()