import pytest

from urll import full_path
from urll.component_bases import Pathname, QueryPart


FULL_PATH_TEXT = '/path/to/resource?key1=value1&key2=value2'


class TestBuiltFromFullPathText:

    @pytest.fixture
    def full_path_inst(self):
        return full_path(FULL_PATH_TEXT)

    def test_has_full_path_text_as_stringval(self, full_path_inst):
        assert str(full_path_inst) == FULL_PATH_TEXT

    def test_exposes_pathname(self, full_path_inst):
        pathname = full_path_inst.pathname
        assert isinstance(pathname, Pathname)
        assert str(pathname) == '/path/to/resource'

    def test_exposes_query_part(self, full_path_inst):
        query_part = full_path_inst.query_part
        assert isinstance(query_part, QueryPart)
        assert str(query_part) == '?key1=value1&key2=value2'
