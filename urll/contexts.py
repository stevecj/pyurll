from . import component_bases as _cb


class SimpleURLContext:

    def url(self, url_text):
        return _cb.URL(self, url_text)

    def network_url(self, network_url_text):
        return _cb.NetworkURL(self, network_url_text)

    def fragment_part(self, fragment_part_text):
        return _cb.FragmentPart(self, fragment_part_text)

    def fragment(self, fragment_text):
        return _cb.Fragment(self, fragment_text)

    def origin(self, origin_text):
        return _cb.Origin(self, origin_text)

    def full_path(self, full_path_text):
        return _cb.FullPath(self, full_path_text)

    def scheme_part(self, scheme_part_text):
        return _cb.SchemePart(self, scheme_part_text)

    def scheme(self, scheme_text):
        return _cb.Scheme(self, scheme_text)

    def netloc(self, netloc_text):
        return _cb.Netloc(self, netloc_text)

    def pathname(self, pathname_text):
        return _cb.Pathname(self, pathname_text)

    def query_part(self, query_part_text):
        return _cb.QueryPart(self, query_part_text)

    def query(self, query_text):
        return _cb.Query(self, query_text)

    def hostname(self, hostname_text):
        return _cb.Hostname(self, hostname_text)

    def port_part(self, port_part_text):
        return _cb.PortPart(self, port_part_text)

    def port(self, port_value):
        return _cb.Port(self, port_value)
