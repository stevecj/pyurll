from urllib.parse import urlparse


class URL:
    def __init__(self, url_text):
        self._init_text = url_text
        parsed = urlparse(url_text)
        for k, v in parsed._asdict().items():
            setattr(self, f'_{k}', v)

    def __str__(self):
        return self._init_text

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
        parsed = urlparse(network_url_text)

        self._scheme = parsed.scheme
        self._netloc = parsed.netloc
        self._path   = parsed.path
        self._query  = parsed.query

    def __str__(self):
        return self._init_text

    @property
    def origin(self):
        return Origin(f'{self._scheme}://{self._netloc}')

    @property
    def full_path(self):
        return FullPath(f'{self._path}?{self._query}')


class FragmentPart:
    def __init__(self, fragment_part_text):
        self._init_text = fragment_part_text

    def __str__(self):
        return self._init_text

    @property
    def fragment(self):
        return Fragment(self._init_text[1:])


class Fragment:
    def __init__(self, fragment_text):
        self._init_text = fragment_text

    def __str__(self):
        return self._init_text


class Origin:
    def __init__(self, origin_text):
        self._init_text = origin_text
        parsed = urlparse(origin_text)

        self._scheme = parsed.scheme
        self._netloc = parsed.netloc

    def __str__(self):
        return self._init_text

    @property
    def scheme_part(self):
        return SchemePart(f'{self._scheme}://')

    @property
    def netloc(self):
        return Netloc(self._netloc)


class FullPath:
    def __init__(self, full_path_text):
        self._init_text = full_path_text
        parsed = urlparse(full_path_text)

        self._path = parsed.path
        self._query = parsed.query

    def __str__(self):
        return self._init_text

    @property
    def pathname(self):
        return Pathname(self._path)

    @property
    def query_part(self):
        return QueryPart(f'?{self._query}')


class SchemePart:
    def __init__(self, scheme_part_text):
        self._init_text = scheme_part_text

    def __str__(self):
        return self._init_text


class Netloc:
    def __init__(self, netloc_text):
        self._init_text = netloc_text

    def __str__(self):
        return self._init_text


class Pathname:
    def __init__(self, netloc_text):
        self._init_text = netloc_text

    def __str__(self):
        return self._init_text


class QueryPart:
    def __init__(self, querypart_text):
        self._init_text = querypart_text

    def __str__(self):
        return self._init_text
