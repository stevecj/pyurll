from urllib.parse import urlparse


class URL:
    def __init__(self, url_text):
        parsed = urlparse(url_text)
        for k, v in parsed._asdict().items():
            setattr(self, f'_{k}', v)

    @property
    def network_url(self):
        return NetworkURL(
            f'{self._scheme}://{self._netloc}{self._path}?{self._query}'
        )

    @property
    def fragment_part(self):
        return FragmentPart(f'#{self._fragment}')


class NetworkURL:
    def __init__(self, network_url_text):
        self._init_text = network_url_text

    def __str__(self):
        return self._init_text


class FragmentPart:
    def __init__(self, fragment_part_text):
        self._init_text = fragment_part_text

    def __str__(self):
        return self._init_text
