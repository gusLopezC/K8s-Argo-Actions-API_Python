from flask import Flask, jsonify
import datetime
import socket
import random


app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! <3 .................',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')

def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

@app.route('/api/v1/users')
def users():
    # Simulated user data
    mock_users = [
        {
            'id': 1,
            'name': 'Juan Pérez',
            'email': 'juan.perez@example.com',
            'role': 'admin',
            'created_at': '2024-01-15T10:30:00Z',
            'status': 'active'
        },
        {
            'id': 2,
            'name': 'María García',
            'email': 'maria.garcia@example.com',
            'role': 'user',
            'created_at': '2024-02-20T14:45:00Z',
            'status': 'active'
        },
        {
            'id': 3,
            'name': 'Carlos López',
            'email': 'carlos.lopez@example.com',
            'role': 'moderator',
            'created_at': '2024-03-10T09:15:00Z',
            'status': 'inactive'
        },
        {
            'id': 4,
            'name': 'Ana Rodríguez',
            'email': 'ana.rodriguez@example.com',
            'role': 'user',
            'created_at': '2024-04-05T16:20:00Z',
            'status': 'active'
        },
        {
            'id': 5,
            'name': 'Luis Martínez',
            'email': 'luis.martinez@example.com',
            'role': 'user',
            'created_at': '2024-05-12T11:00:00Z',
            'status': 'active'
        }
    ]
    
    return jsonify({
        'users': mock_users,
        'total_count': len(mock_users),
        'timestamp': datetime.datetime.now().isoformat(),
        'data_source': 'simulated'
    })

if __name__ == '__main__':

    app.run(host="0.0.0.0")

