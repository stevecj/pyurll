import pytest

from urll import scheme_part
from urll.component_bases import Scheme


SCHEME_PART_TEXT = 'http://'


class TestBuiltFromSchemePartText:

    @pytest.fixture
    def scheme_part_inst(self):
        return scheme_part(SCHEME_PART_TEXT)

    def test_has_scheme_part_text_as_stringval(self, scheme_part_inst):
        assert str(scheme_part_inst) == SCHEME_PART_TEXT

    def test_exposes_scheme(self, scheme_part_inst):
        scheme = scheme_part_inst.scheme
        assert isinstance(scheme, Scheme)
        assert str(scheme) == 'http'
