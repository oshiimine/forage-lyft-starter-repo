from tire.tire import Tire
from constants import Constants


class OctoprimeTire(Tire):
    def __init__(self, tireArray):
        self.tireArray = tireArray

    def needs_service(self):
        return sum(self.tireArray) >= Constants.octoprimeTotalTireRequirement
