from tire.tire import Tire
from constants import Constants


class CarriganTire(Tire):
    def __init__(self, tireArray):
        self.tireArray = tireArray

    def needs_service(self):
        return max(self.tireArray) >= Constants.carriganPerTireRequirement
