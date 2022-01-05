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
        parsed = urlparse(scheme_part_text)

        self._scheme = parsed.scheme

    def __str__(self):
        return self._init_text

    @property
    def scheme(self):
        return Scheme(self._scheme)


class Scheme:
    def __init__(self, scheme_text):
        self._init_text = scheme_text

    def __str__(self):
        return self._init_text


class Netloc:
    def __init__(self, netloc_text):
        self._init_text = netloc_text

    def __str__(self):
        return self._init_text

    @property
    def hostname(self):
        return Hostname(self._init_text.split(':')[0])

    @property
    def port_part(self):
        return PortPart(':' + self._init_text.split(':')[1])


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

    @property
    def query(self):
        return Query(self._init_text[1:])


class Query:
    def __init__(self, query_text):
        self._init_text = query_text

    def __str__(self):
        return self._init_text


class Hostname:
    def __init__(self, hostname_text):
        self._init_text = hostname_text

    def __str__(self):
        return self._init_text


class PortPart:
    def __init__(self, port_part_text):
        self._init_text = port_part_text

    def __str__(self):
        return self._init_text

    @property
    def port(self):
        return Port(self._init_text[1:])


class Port:
    def __init__(self, port_value):
        if port_value is None or port_value == '':
            self._number = None
        elif isinstance(port_value, int):
            # Values of other types such as bool are treated as actual
            # or virtual sublasses of int so should be accepted but
            # converted to the actual int type.
            self._number = int(port_value)
        elif isinstance(port_value, str):
            self._number = int(port_value)
        else:
            raise TypeError(
                f'port_value must be int or str type, not {port_value!r}')

        if self._number is not None and not (0 <= self._number <= 0xffff):
            raise ValueError(
                'port_value must be between 0 and 65535 (inclusive)')

    def __str__(self):
        if self._number is None:
            return ''
        else:
            return str(self._number)

    def __int__(self):
        if self._number is None:
            raise ValueError(
                'Null instance of Port cannot be converted to integer')
        return self._number

    @property
    def number(self):
        return self._number

    def __bool__(self):
        return self._number is not None
