import pytest

from urll import URL


FULL_URL_TEXT = (
    'http://www.example.com:80/path/to/resource'
    '?key1=value1&key2=value2#PlaceInDocument'
)


class TestBuiltFromFullURL:

    @pytest.fixture
    def url_inst(self):
        return URL(FULL_URL_TEXT)

    def test_exposes_network_url(self, url_inst):
        assert str(url_inst.network_url) == (
            'http://www.example.com:80/path/to/resource'
            '?key1=value1&key2=value2'
        )

    def test_exposes_fragment_part(self, url_inst):
        assert str(url_inst.fragment_part) == '#PlaceInDocument'
