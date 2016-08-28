"""
Flask server for converting OpsGenie hooks into WebSockets for an Internet of
Things device.
"""

import eventlet
eventlet.monkey_patch()

# pylint:disable=wrong-import-position
from flask import Flask, render_template
from flask_socketio import SocketIO
# pylint:enable=wrong-import-position

# pylint:disable=invalid-name
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
# pylint:enable=invalid-name


@app.route('/')
def index():
    """
    Serve a JS page that upgrades you to a websocket.
    """

    return render_template('index.html')


@app.route('/notify')
def notify():
    """
    HTTP request called by the webhook.

    Emits a WebSocket event to connected clients.
    """
    print("Notify")
    socketio.emit('alert')

    return "Ok!"


@socketio.on('connect')
def connect():
    """
    WebSocket client connected.
    """
    print("New connection")


if __name__ == '__main__':
    print("Starting server")
    socketio.run(app, debug=True, use_reloader=True)