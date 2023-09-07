from utils import utils


def test_reversed():
    utility = utils()
    # test string
    reversed = utility.reversed("test")
    assert reversed == -1
    # test float
    reversed = utility.reversed(123.4)
    assert reversed == -1
    # test integer
    reversed = utility.reversed(123)
    assert reversed == 321


def test_formatter():
    utility = utils()
    # test string
    binary, octal = utility.formatter("test")
    assert binary == -1
    assert octal == -1
    # test float
    binary, octal = utility.formatter(123.4)
    assert binary == -1
    assert octal == -1
    # test integer
    binary, octal = utility.formatter(10)
    assert binary == "0b1010"
    assert octal == "012"


test_reversed()
test_formatter()
