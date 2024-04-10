from lib.tyre import *
import datetime
import pytest

def test_tyre_pos_init():
    tyre = Tyre('FL', 50, 180, '2024-04-10')
    assert tyre.tyre_position == 'FL'
    assert tyre.tread_depth == 50
    assert tyre.pressure == 180
    assert tyre.date == '2024-04-10'

def test_tyre_position_is_correct_string():
    with pytest.raises(ValueError) as e:
        tyre = Tyre(0, 50, 180, '2024-04-10')
    error_message = str(e.value)
    assert error_message == "Tyre position must be either FR, FL, BL, BR"

def test_tread_depth_is_int():
    with pytest.raises(ValueError) as e:
        tyre = Tyre('FR', '50', 180, '2024-04-10')
    error_message = str(e.value)
    assert error_message == "Tread depth must be of type int."

def test_pressure_is_int():
    with pytest.raises(ValueError) as e:
        tyre = Tyre('FR', 50, '180', '2024-04-10')
    error_message = str(e.value)
    assert error_message == "Tread depth must be of type int."

def test_date_is_in_correct_format():
    with pytest.raises(ValueError) as e:
        Tyre('FR', 50, 180, '202323-10')
    error_message = str(e.value)
    assert error_message == "Date must be in format YYYY-MM-DD"