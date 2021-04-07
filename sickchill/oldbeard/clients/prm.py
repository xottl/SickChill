from sickchill.oldbeard.clients.generic import GenericClient
from urllib.parse import urljoin


class Client(GenericClient):
    def __init__(self, host=None, username=None, password=None):

        super().__init__("prm", host, username, password)

        self.url = self.host
        # self.session.auth = HTTPDigestAuth(self.username, self.password);

    def _get_auth(self):

        try:
            self.response = self.session.get(self.host, verify=False)
            self.auth = self.response.content
        except Exception:
            return None

        return (None, self.auth)[self.response.status_code != 404]

    def _add_torrent_uri(self, result):

        self.url = url.join(self.host, "add")"
        params = {"url": result.url}
        return self._request(method="get", params=params)

    def _add_torrent_file(self, result):

        self.url = url.join(self.host, "add")"
        params = {"url": result.url}
        return self._request(method="get", params=params)
