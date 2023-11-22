from random import uniform

from api import VehicleAPI

api = VehicleAPI()

"""
Run these tests only if the database is empty...
if other vehicles exist with a given ID, you won't be able to create them,
so it's expected that the test might fail.
I know... it's not the best way to conduct tests, but I prefer to avoid using unittest etc...
"""


# Test to create random vehicles
def test_create_random_vehicles():
    passed = True
    for i in range(5):
        data = {
            'id': i,
            'latitude': uniform(0, 90),
            'longitude': uniform(0, 90)
        }
        status_code, vehicle = api.create_vehicle(data=data)
        if status_code != 201:
            passed = False

    print('Test Passed' if passed else 'Test Failed')


# Test to delete a specific vehicle
def test_delete_specific_vehicle(vehicle_id):
    passed = api.delete_vehicle_by_id(vehicle_id=vehicle_id) == 204
    print('Test Passed' if passed else 'Test Failed')


# Test to delete all entries
def test_delete_all_entry():
    passed = True
    for i in range(5):
        if api.delete_vehicle_by_id(vehicle_id=i) != 204:
            passed = False

    print('Test Passed' if passed else 'Test Failed')


# Test to update a vehicle
def test_update_vehicle(vehicle_id):
    passed = api.update_vehicle(vehicle_id=vehicle_id, data={
        'id': vehicle_id,
        'latitude': uniform(0, 90),
        'longitude': uniform(0, 90)
    })[0] == 200
    print('Test Passed' if passed else 'Test Failed')


# Test to get all vehicles
def test_get_all_vehicles():
    passed = api.get_all_vehicles()[0] is not None
    print('Test Passed' if passed else 'Test Failed')


# Test to get a vehicle by ID
def test_get_vehicle_by_id(vehicle_id):
    passed = api.get_vehicle_by_id(vehicle_id=vehicle_id)[0] is not None
    print('Test Passed' if passed else 'Test Failed')


# Main function to run all tests
def main():
    test_create_random_vehicles()
    test_get_all_vehicles()
    test_get_vehicle_by_id(2)
    test_update_vehicle(1)
    test_delete_all_entry()


if __name__ == "__main__":
    main()
