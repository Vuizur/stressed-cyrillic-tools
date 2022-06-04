from stressed_cyrillic_tools import __version__
from stressed_cyrillic_tools.tools import is_acute_accented


def test_version():
    assert __version__ == '0.1.0'

def test_is_acute_accented():
    assert is_acute_accented('без') == False
    assert is_acute_accented('без ударения') == False
    assert is_acute_accented("склоне́ние") == True