import pytest

from urll import port_part
from urll.component_bases import Port


PORT_PART_TEXT = ':80'


class TestBuiltFromPortPartText:

    @pytest.fixture
    def port_part_inst(self):
        return port_part(PORT_PART_TEXT)

    def test_has_port_part_text_as_stringval(self, port_part_inst):
        assert str(port_part_inst) == PORT_PART_TEXT

    def test_exposes_port(self, port_part_inst):
        port = port_part_inst.port
        assert isinstance(port, Port)
        assert str(port) == '80'
