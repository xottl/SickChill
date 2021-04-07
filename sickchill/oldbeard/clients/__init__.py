from collections import OrderedDict
from sickchill import logger

_clients = sorted(["utorrent", "transmission", "deluge", "deluged", "download_station", "rtorrent", "qbittorrent", "mlnet", "putio", "prm"])


default_host = {
    "utorrent": "http://localhost:8000",
    "transmission": "http://localhost:9091",
    "deluge": "http://localhost:8112",
    "deluged": "scgi://localhost:58846",
    "download_station": "http://localhost:5000",
    "rtorrent": "scgi://localhost:5000",
    "qbittorrent": "http://localhost:8080",
    "mlnet": "http://localhost:4080",
    "putio": "https://api.put.io/login",
    "prm": "http://localhost:8000"
}


def getClientInstance(name):
    return __import__("sickchill.oldbeard.clients." + name.lower(), fromlist=_clients).Client


def getClientListDict(keys_only=False):
    if keys_only:
        return _clients + ["blackhole"]

    result = OrderedDict()
    result["blackhole"] = "Black Hole"
    for client in _clients:
        result[client] = getClientInstance(client)().name
        logger.debug("adding client " + result[client])
    return result
