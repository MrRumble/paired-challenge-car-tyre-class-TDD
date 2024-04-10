from datetime import datetime

class Tyre:
    def __init__(self, tyre_position, tread_depth, pressure, date):
        tyre_positions = ['FR', 'FL', 'BL', 'BR']
        if tyre_position not in tyre_positions:
            raise ValueError("Tyre position must be either FR, FL, BL, BR")
        if type(tread_depth) is not int or type(pressure) is not int:
            raise ValueError("Tread depth must be of type int.")
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except:
            raise ValueError("Date must be in format YYYY-MM-DD")




        self.tread_depth = tread_depth
        self.tyre_position = tyre_position
        self.pressure = pressure
        self.date = date

    