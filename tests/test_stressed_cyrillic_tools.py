from stressed_cyrillic_tools import __version__
from stressed_cyrillic_tools import (
    get_lower_and_without_yo,
    is_acute_accented,
    has_two_stress_marks,
    fix_two_accent_marks,
)


def test_version():
    assert __version__ == "0.1.0"


def test_is_acute_accented():
    assert is_acute_accented("без") == False
    assert is_acute_accented("без ударения") == False
    assert is_acute_accented("склоне́ние") == True


def test_is_lower_and_without_yo():
    assert get_lower_and_without_yo("Москва́") == "москва"


def test_has_two_stress_marks():
    assert has_two_stress_marks("склоне́ние") == False
    assert has_two_stress_marks("склоне́ние́") == True
    # Here no baked in version for the grave accent exists
    assert has_two_stress_marks("зу̀бофрезерова́ние") == True
    assert has_two_stress_marks("зу̀б") == False
    # Here a baked in version exists
    assert has_two_stress_marks("мѐгане́кко") == True
    assert has_two_stress_marks("мѐг") == False


def test_fix_two_accent_marks():
    assert fix_two_accent_marks("склоне́ние́") == "склоне́ние"
    assert fix_two_accent_marks("зу̀бофрезерова́ние") == "зубофрезерова́ние"
    assert fix_two_accent_marks("мѐгане́кко") == "мегане́кко"
    assert fix_two_accent_marks("мѐг") == "мѐг"
