import pytest

from urll import Fragment, FragmentPart


FRAGMENT_PART_TEXT = '#PlaceInDocument'


class TestBuiltFromFragmentPartText:

    @pytest.fixture
    def fragment_part_inst(self):
        return FragmentPart(FRAGMENT_PART_TEXT)

    def test_has_fragment_part_text_as_stringval(self, fragment_part_inst):
        assert str(fragment_part_inst) == FRAGMENT_PART_TEXT

    def test_exposes_fragment(self, fragment_part_inst):
        fragment = fragment_part_inst.fragment
        assert isinstance(fragment, Fragment)
        assert str(fragment) == 'PlaceInDocument'
