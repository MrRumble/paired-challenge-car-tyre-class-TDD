from lib.tyre import *
from lib.car_owner import *

def test_init_with_tyres_list():
    car_owner = CarOwner()
    assert car_owner.tyres == []
