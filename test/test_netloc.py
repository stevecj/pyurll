import pytest

from urll import netloc
from urll.component_bases import Hostname, PortPart


NETLOC_TEXT = 'www.example.com:80'


class TestBuiltFromNetlocText:

    @pytest.fixture
    def netloc_inst(self):
        return netloc(NETLOC_TEXT)

    def test_has_netloc_text_as_stringval(self, netloc_inst):
        assert str(netloc_inst) == NETLOC_TEXT

    def test_exposes_hostname(self, netloc_inst):
        hostname = netloc_inst.hostname
        assert isinstance(hostname, Hostname)
        assert str(hostname) == 'www.example.com'

    def test_exposes_port_part(self, netloc_inst):
        port_part = netloc_inst.port_part
        assert isinstance(port_part, PortPart)
        assert str(port_part) == ':80'
