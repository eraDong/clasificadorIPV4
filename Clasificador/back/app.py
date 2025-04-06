from flask import Flask, request, jsonify
from flask_cors import CORS
from logica import *  # Importar funciones

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/analizar": {"origins": "https://m4nu0113.github.io"}})

@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.json
    ip = data.get('ip')
    
    if not ip or not ipValidation(ip):  # Usa la función de validación
        return jsonify({"error": "IP no válida"}), 400
    
    # Usa las funciones de lógica
    response = {
        "Clase": buscarClase(ip),
        "Tipo": buscarTipo(ip),
        "Estructura": devolverEstructura(ip),
        "Dirección de Red": devolverDirRed(ip),
        "Dirección de Broadcast": devolverDirBroadcast(ip),
        "Máscara de Subred": devolverMascara(ip),
        "Dirección de Hosts": devolverDirHosts(ip)
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)