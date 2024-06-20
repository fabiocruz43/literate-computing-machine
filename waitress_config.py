import sys
import os
from waitress import serve

# Adicione o diretório raiz ao Python path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

# Importe a variável app do módulo app.py
from app import app

# Verifique se a variável app está definida corretamente
if not hasattr(app, 'run'):
    raise RuntimeError("A variável 'app' não está definida corretamente.")

# Configuração do servidor Waitress
if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8080)

