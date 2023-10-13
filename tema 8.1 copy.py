from flask import Flask, request

app = Flask(__name__)

@app.route('/info', methods=["GET", "POST"])
def inicio():
    cad = ""
    cad += "URL:" + request.url + "\n"
    cad += "Método:" + request.method + "\n"
    
    cad += "header:\n"
    for item, value in request.headers.items():
        cad += "{}:{}\n".format(item, value)
    
    cad += "información en formularios (POST):\n"
    for item, value in request.form.items():
        cad += "{}:{}\n".format(item, value)
    
    cad += "información en URL (GET):\n"
    for item, value in request.args.items():
        cad += "{}:{}\n".format(item, value)
    
    cad += "Ficheros:\n"
    for item, value in request.files.items():
        cad += "{}:{}\n".format(item, value)
    return cad

@app.route('/articulos/')
def articulos():
    return 'Lista de artículos'

@app.route('/articulos/new', methods=["POST"])
def articulos_new():
    return 'Está URL recibe información de un formulario con el método POST'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Hemos accedido con POST'
    else:
        return 'Hemos accedido con GET'

if __name__ == '__main__':
    app.run()