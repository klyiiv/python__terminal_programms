# тренировка ооп наследование

class Transport:
 
    def move(self):
        pass
 
 
class WaterTransport(Transport):
 
    def swim(self):
        pass
 
 
class Parom(WaterTransport):
 
    pass
 
 
class Ship(WaterTransport):
 
    pass
 
 
class BoatShip(Ship):
 
    pass
 
 
class MotorShip(Ship):
 
    pass
 
 
class Lodka(WaterTransport):
 
    pass
 
 
class WarShip(MotorShip):
 
    def gun(self):
        pass
 
 
class TransportShip(MotorShip):
 
    pass
 
 
class PeopleShip(MotorShip):
 
    pass
 
 
class SpaceTransport(Transport):
 
    def fly_high(self):
        pass
 
 
class Rocket(SpaceTransport):
 
    pass
 
 
class Shuttle(SpaceTransport):
 
    pass
 
 
class Falcon(SpaceTransport):
 
    def space_x(self):
        pass
 
 
class FalconHeavy(Falcon):
 
    pass
 
 
class SpaceDragon(Falcon):
 
    pass
 
 
class SkyTransport(Transport):
 
    def fly(self):
        pass
 
 
class Vertolet(SkyTransport):
 
    pass
 
 
class Plane(SkyTransport):
 
    pass
 
 
class WarPlane(Plane):
 
    def gun(self):
        pass
 
 
class TransportPlane(Plane):
 
    pass
 
 
class PeoplePlane(Plane):
 
    pass
 
 
class Deltaplane(SkyTransport):
 
    pass
 
 
class Ballon(SkyTransport):
 
    pass
 
 
class GroundTransport(Transport):
 
    def drive(self):
        pass
 
 
class EngineGroundTransport(GroundTransport):
 
    def engine(self):
        pass
 
 
class HeavyAuto(EngineGroundTransport):
 
    pass
 
 
class LigthAuto(EngineGroundTransport):
 
    pass
 
 
class Bus(HeavyAuto):
 
    pass
 
 
class Train(EngineGroundTransport):
 
    pass
 
 
class TownTrain(Train):
 
    pass
 
 
class BuildingTransport(HeavyAuto):
 
    pass
 
 
class Bike(GroundTransport):
 
    pass
 
 
class TrolleyBus(Bus):
 
    pass
