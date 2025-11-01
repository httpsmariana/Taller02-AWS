import socket
def get_container_id() -> str:
    try:
        return socket.gethostname()
    except Exception:
        return "unknown"
