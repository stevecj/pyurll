import pytest

from urll import query_part
from urll.component_bases import Query


QUERY_PART_TEXT = '#PlaceInDocument'


class TestBuiltFromQueryPartText:

    @pytest.fixture
    def query_part_inst(self):
        return query_part(QUERY_PART_TEXT)

    def test_has_query_part_text_as_stringval(self, query_part_inst):
        assert str(query_part_inst) == QUERY_PART_TEXT

    def test_exposes_query(self, query_part_inst):
        query = query_part_inst.query
        assert isinstance(query, Query)
        assert str(query) == 'PlaceInDocument'
