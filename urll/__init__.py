from .contexts import SimpleURLContext


_default_url_context = SimpleURLContext()


def url(url_text):
    return _default_url_context.url(url_text)


def network_url(network_url_text):
    return _default_url_context.network_url(network_url_text)


def fragment_part(fragment_part_text):
    return _default_url_context.fragment_part(fragment_part_text)


def fragment(fragment_text):
    return _default_url_context.fragment(fragment_text)


def origin(origin_text):
    return _default_url_context.origin(origin_text)


def full_path(full_path_text):
    return _default_url_context.full_path(full_path_text)


def scheme_part(scheme_part_text):
    return _default_url_context.scheme_part(scheme_part_text)


def scheme(scheme_text):
    return _default_url_context.scheme(scheme_text)


def netloc(netloc_text):
    return _default_url_context.netloc(netloc_text)


def pathname(pathname_text):
    return _default_url_context.pathname(pathname_text)


def query_part(query_part_text):
    return _default_url_context.query_part(query_part_text)


def query(query_text):
    return _default_url_context.query(query_text)


def hostname(hostname_text):
    return _default_url_context.hostname(hostname_text)


def port_part(port_part_text):
    return _default_url_context.port_part(port_part_text)


def port(port_value):
    return _default_url_context.port(port_value)
