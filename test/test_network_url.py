import pytest

from urll import NetworkURL, Origin, FullPath


NETWORK_URL_TEXT = (
    'http://www.example.com:80/path/to/resource'
    '?key1=value1&key2=value2'
)


class TestBuiltFromFullURL:

    @pytest.fixture
    def netwk_url_inst(self):
        return NetworkURL(NETWORK_URL_TEXT)

    def test_has_network_url_text_as_stringval(self, netwk_url_inst):
        assert str(netwk_url_inst) == NETWORK_URL_TEXT

    def test_exposes_origin(self, netwk_url_inst):
        origin = netwk_url_inst.origin
        assert isinstance(origin, Origin)
        assert str(origin) == 'http://www.example.com:80'

    def test_exposes_full_path(self, netwk_url_inst):
        full_path = netwk_url_inst.full_path
        assert isinstance(full_path, FullPath)
        assert str(full_path) == '/path/to/resource?key1=value1&key2=value2'
