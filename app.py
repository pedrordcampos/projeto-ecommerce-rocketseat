# Importação
from flask import Flask

app = Flask(__name__)

# Definir a rota
@app.route('/')
def helloworld():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)
