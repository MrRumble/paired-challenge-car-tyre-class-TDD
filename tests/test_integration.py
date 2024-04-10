from lib.car_owner import *
from lib.tyre import *

def test_one_tyre_added_to_self_list():
    car_owner = CarOwner()
    tyre = Tyre('FL', 40, 40, "2020-09-13")
    car_owner.add_tyre(tyre)
    assert car_owner.tyres == [tyre]

def test_get_pressure_from_one_tyre_in_list():
    car_owner = CarOwner()
    tyre = Tyre('FL', 40, 40, "2020-09-13")
    car_owner.add_tyre(tyre)
    assert car_owner.get_tyre_pressure('FL') == {"2020-09-13" : 40}

def test_get_pressure_with_two_tyres_in_list():
    car_owner = CarOwner()
    tyre = Tyre('FL', 40, 40, "2020-09-13")
    tyre2 = Tyre('FL', 50, 50, "2020-09-14")
    car_owner.add_tyre(tyre)
    car_owner.add_tyre(tyre2)
    assert car_owner.get_tyre_pressure('FL') == {"2020-09-13" : 40, "2020-09-14" : 50 }

def test_message_sent_when_tyre_pressure_has_no_historical_readings():
    car_owner = CarOwner()
    assert car_owner.get_tyre_pressure('FL') == 'No historical data for this tyre.'

def test_get_depth_with_two_tyres_in_list():
    car_owner = CarOwner()
    tyre = Tyre('FR', 40, 40, "2020-09-13")
    tyre2 = Tyre('FR', 50, 50, "2020-09-14")
    car_owner.add_tyre(tyre)
    car_owner.add_tyre(tyre2)
    assert car_owner.get_tyre_tread_depth('FR') == {"2020-09-13" : 40, "2020-09-14" : 50 }

def test_get_depth_with_multiple_tyres_in_list():
    car_owner = CarOwner()
    tyre = Tyre('FR', 40, 40, "2020-09-13")
    tyre2 = Tyre('FR', 50, 50, "2020-09-14")
    tyre3 = Tyre('FL', 40, 40, "2020-09-13")
    tyre4 = Tyre('BR', 50, 50, "2020-09-14")
    car_owner.add_tyre(tyre)
    car_owner.add_tyre(tyre2)
    car_owner.add_tyre(tyre3)
    car_owner.add_tyre(tyre4)
    assert car_owner.get_tyre_tread_depth('FR') == {"2020-09-13" : 40, "2020-09-14" : 50 }
    