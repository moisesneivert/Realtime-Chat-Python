from flask_socketio import emit
from app.server import socketio

@socketio.on("message")
def handle_message(msg):
    """
    Evento disparado quando um usuário envia uma mensagem.
    A mensagem é retransmitida para todos os clientes conectados.
    """
    emit("message", msg, broadcast=True)
