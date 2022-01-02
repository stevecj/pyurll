from urllib.parse import urlparse


class URL:
    def __init__(self, url_text):
        parsed = urlparse(url_text)
        for k, v in parsed._asdict().items():
            setattr(self, f'_{k}', v)

    @property
    def network_url(self):
        return f'{self._scheme}://{self._netloc}{self._path}?{self._query}'

    @property
    def fragment_part(self):
        return f'#{self._fragment}'
