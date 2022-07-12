import pytest
from scanner_handle import CheckQr


def test_check_len_color():
    checkqr = CheckQr()

    for color, result in [
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('seven_c', 'Fuzzy Wuzzy'),
    ]:
        assert checkqr.check_len_color(color) == result


def test_check_len_color_not_exist():
    checkqr = CheckQr()

    for not_exist, result in [
        ('not_exist', None),
        ('not_exist2', None),
        ('not_exist3', None),
        ('not_exist4', None),
    ]:
        assert checkqr.check_len_color(not_exist) == result


#bypassed the check_in_db method
@pytest.mark.skip(reason="no way of currently testing this")
def test_check_color(mocker):
    checkqr = CheckQr()

    mocker.patch(
        'scanner_handle.CheckQr.check_in_db',
        return_value=True
    )

    for color, result in [
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('seven_c', 'Fuzzy Wuzzy'),
    ]:
        assert checkqr.check_scanned_device(color) == result
