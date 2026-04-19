from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renderizamos el archivo que está en la carpeta /templates
    return render_template('index.html')

if __name__ == '__main__':
    # El modo debug es ideal para desarrollo (recarga sola al guardar)
    app.run(debug=True, host='0.0.0.0', port=8080)