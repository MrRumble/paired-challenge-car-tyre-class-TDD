from lib.tyre import *

class CarOwner:
    def __init__(self):
        self.tyres = []

    def add_tyre(self, tyre):
        self.tyres.append(tyre)

    def get_tyre_pressure(self, tyre_position):
        tyre_pressures = {}       
        for tyre in self.tyres:
            if tyre.tyre_position == tyre_position:
                tyre_pressures[tyre.date] = tyre.pressure
        if tyre_pressures != {}:
            return tyre_pressures
        else:
            return 'No historical data for this tyre.'

    
    def get_tyre_tread_depth(self, tyre_position):
        tyre_treads = {}
        for tyre in self.tyres:
            if tyre.tyre_position == tyre_position:
                tyre_treads[tyre.date] = tyre.tread_depth
        if tyre_treads != {}:
            return tyre_treads
        else:
            return 'No historical data for this tyre.'
        

