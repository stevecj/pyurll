import pytest

from urll import Netloc, Origin, SchemePart


ORIGIN_TEXT = 'http://www.example.com:80'


class TestBuiltFromOriginText:

    @pytest.fixture
    def origin_inst(self):
        return Origin(ORIGIN_TEXT)

    def test_has_origin_text_as_stringval(self, origin_inst):
        assert str(origin_inst) == ORIGIN_TEXT

    def test_exposes_scheme_part(self, origin_inst):
        scheme_part = origin_inst.scheme_part
        assert isinstance(scheme_part, SchemePart)
        assert str(scheme_part) == 'http://'

    def test_exposes_netloc(self, origin_inst):
        netloc = origin_inst.netloc
        assert isinstance(netloc, Netloc)
        assert str(netloc) == 'www.example.com:80'
