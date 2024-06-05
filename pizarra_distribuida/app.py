from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('draw', namespace='/draw')
def draw(message):
    socketio.emit('draw', message, namespace='/draw')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
