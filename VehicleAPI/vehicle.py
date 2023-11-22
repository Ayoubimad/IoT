class Vehicle:
    def __init__(self):
        self.id = None
        self.latitude = None
        self.longitude = None

    def serialize(self):
        return str({
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude
        })

    def __str__(self):
        return self.serialize()


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_info):
        vehicle = Vehicle()
        vehicle.id = vehicle_info.get("id")
        vehicle.latitude = vehicle_info.get("latitude")
        vehicle.longitude = vehicle_info.get("longitude")
        return vehicle
