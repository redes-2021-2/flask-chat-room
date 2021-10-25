from flask.globals import session
from flask_socketio import emit, join_room, leave_room, rooms
from .. import socketio

@socketio.on('joined', namespace='/chat')
def joined(message):
    """[Cuando entre un cliente a la sala
        El estatus del mensaje se envia a todos los demas miembros]
    Args:
        message ([string]): [mensaje de entrada]
    """
    room = session.get("room")
    join_room(room)
    emit('status', {'msg': session.get('name') + " entro a la sala"}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    """[Cuando escriba un nuevo mensaje en la sala
        El estatus del mensaje se envia a todos los demas miembros]
    Args:
        message ([string]): [mensaje de entrada]
    """
    room = session.get("room")
    emit('status', {'msg': session.get('name') +': '+ message.get('msg')}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    """[Cuando abandone un cliente a la sala
        El estatus del mensaje se envia a todos los demas miembros]
    Args:
        message ([string]): [mensaje de entrada]
    """
    room = session.get("room")
    leave_room(room)
    emit('status', {'msg': session.get('name') + " salio de la sala."}, room=room)

    
    