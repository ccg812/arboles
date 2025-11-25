from flask import Flask, render_template, jsonify
import os

# Configuración:
# template_folder='.' -> Busca el HTML en la carpeta actual
# static_folder='.'   -> Sirve archivos estáticos (si hubiera CSS/JS externos) desde aquí
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def home():
    """Ruta principal que carga el visualizador"""
    return render_template('index.html')

@app.route('/api/status')
def system_check():
    """API para simular conexión con el núcleo del sistema"""
    return jsonify({
        "status": "ONLINE",
        "core": "PYTHON_FLASK_V3",
        "latency": "12ms"
    })

if __name__ == '__main__':
    print("\n>>> INICIANDO SISTEMA NEXUS...")
    print(">>> ACCEDE A: http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)