import pytest

from urll import Port


TYPICAL_PORT_NUM  = 123
TYPICAL_PORT_TEXT = '123'
MAX_PORT_NUM  = 0xffff   # 2 ^ 16 - 1
MAX_PORT_TEXT = '65535'  # 2 ^ 16 - 1


class TestInvalidInitialization:

    @pytest.mark.parametrize('init_arg', (
        80.1,
        [],
        lambda x: x))
    def test_rejects_invalid_type(self, init_arg):
        with pytest.raises(TypeError):
            Port(init_arg)

    @pytest.mark.parametrize('init_arg', ('nope', '80.1'))
    def test_rejects_string_not_representing_integer(self, init_arg):
        with pytest.raises(ValueError):
            Port(init_arg)

    @pytest.mark.parametrize('init_arg', (-1, 0x10000))
    def test_rejects_integer_out_of_range(self, init_arg):
        with pytest.raises(ValueError):
            Port(init_arg)

    @pytest.mark.parametrize('init_arg', ('-1', '65536'))
    def test_rejects_string_repr_of_integer_out_of_range(self, init_arg):
        with pytest.raises(ValueError):
            Port(init_arg)


@pytest.mark.parametrize('init_arg', (None, ''))
class TestBuiltAsNullInstance:

    @pytest.fixture
    def port_inst(self, init_arg):
        return Port(init_arg)

    def test_is_falsy(self, port_inst):
        assert bool(port_inst) is False

    def test_has_empty_string_as_stringval(self, port_inst):
        assert str(port_inst) == ''

    def test_has_none_as_number(self, port_inst):
        assert port_inst.number is None

    def test_cannot_be_converted_to_int(self, port_inst):
        with pytest.raises(ValueError):
            int(port_inst)


@pytest.mark.parametrize('init_arg', (0, '0'))
class TestBuildWithMinimumValue:

    @pytest.fixture
    def port_inst(self, init_arg):
        return Port(init_arg)

    def test_is_truthy(self, port_inst):
        assert bool(port_inst) is True

    def test_has_0_as_stringval(self, port_inst):
        assert str(port_inst) == '0'

    def test_has_zero_as_number(self, port_inst):
        assert port_inst.number == 0

    def test_has_zero_as_intval(self, port_inst):
        assert int(port_inst) == 0


@pytest.mark.parametrize('init_arg', (MAX_PORT_NUM, MAX_PORT_TEXT))
class TestBuildWithMaximumValue:

    @pytest.fixture
    def port_inst(self, init_arg):
        return Port(init_arg)

    def test_is_truthy(self, port_inst):
        assert bool(port_inst) is True

    def test_has_string_repr_of_max_as_stringval(self, port_inst):
        assert str(port_inst) == MAX_PORT_TEXT

    def test_has_max_value_as_number(self, port_inst):
        assert port_inst.number == MAX_PORT_NUM

    def test_has_max_value_as_intval(self, port_inst):
        assert int(port_inst) == MAX_PORT_NUM


@pytest.mark.parametrize('init_arg', (TYPICAL_PORT_NUM, TYPICAL_PORT_TEXT))
class TestBuildWithTypicalValue:

    @pytest.fixture
    def port_inst(self, init_arg):
        return Port(init_arg)

    def test_is_truthy(self, port_inst):
        assert bool(port_inst) is True

    def test_has_string_repr_of_value_as_stringval(self, port_inst):
        assert str(port_inst) == TYPICAL_PORT_TEXT

    def test_has_value_as_number(self, port_inst):
        assert port_inst.number == TYPICAL_PORT_NUM

    def test_has_value_as_intval(self, port_inst):
        assert int(port_inst) == TYPICAL_PORT_NUM
