import pytest

from urll import url
from urll.component_bases import FragmentPart, NetworkURL


FULL_URL_TEXT = (
    'http://www.example.com:80/path/to/resource'
    '?key1=value1&key2=value2#PlaceInDocument'
)


class TestBuiltFromFullURLText:

    @pytest.fixture
    def url_inst(self):
        return url(FULL_URL_TEXT)

    def test_has_full_url_text_as_stringval(self, url_inst):
        assert str(url_inst) == FULL_URL_TEXT

    def test_exposes_network_url(self, url_inst):
        network_url = url_inst.network_url
        assert isinstance(network_url, NetworkURL)
        assert str(network_url) == (
            'http://www.example.com:80/path/to/resource'
            '?key1=value1&key2=value2'
        )

    def test_exposes_fragment_part(self, url_inst):
        fragment_part = url_inst.fragment_part
        assert isinstance(fragment_part, FragmentPart)
        assert str(fragment_part) == '#PlaceInDocument'
