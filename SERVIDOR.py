#//PROGRAMA DEL SERVIDOR//
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
actions =[]

# Configuración de logging
logging.basicConfig(filename='server.log', level=logging.INFO)

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    actions.append(data)
    print(data)
    action = data.get('action')
    if action == 'move':
        direction = data.get('direction')
        position = data.get('position')
        logging.info(f'Move action: {direction} to position {position}')
        return jsonify({"status": "success", "action": "move", "direction": direction, "position": position})
    elif action == 'photo':
        photo_data = data.get('data')
        position = data.get('position')
        logging.info(f'Photo action received at position {position}')
        # Validar código ARUCO aquí
        return jsonify({"status": "success", "action": "photo", "position": position})
    return jsonify({"status": "error", "message": "Invalid action"})

@app.route('/actions', methods=['GET'])
def get_actions():
    return jsonify(actions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)