class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.system = {
            1 : big, 
            2 : medium, 
            3 : small
        }

    def addCar(self, carType: int) -> bool:
        if self.system[carType]:
            self.system[carType] -= 1
            return True
        return False
