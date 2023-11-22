import json
from configparser import ConfigParser

import requests

from vehicle import VehicleFactory

# Reads server configuration from an ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Extracts fields from the config file
FIELDS = []
if "FIELDS" in config_object:
    fields_section = config_object["FIELDS"]
    FIELDS = [fields_section[field] for field in fields_section]

# Builds the URI for API requests using config values
server = config_object["SERVERCONFIG"]
URI = ' http://' + server["HOST"] + ':' + server["PORT"] + '/' + server["ENDPOINT"]


class VehicleAPI:
    def __init__(self, url=URI):
        self.url = url

    def get_all_vehicles(self):
        """
        Retrieves all vehicles from the API.

        :return: Tuple (status_code, vehicle objects) or (status_code, None)
        """
        response = requests.get(url=self.url)
        if response.status_code == 200:
            vehicles_info = response.json()
            vehicles = [VehicleFactory.create_vehicle(vehicle_info) for vehicle_info in vehicles_info]
            return response.status_code, vehicles
        else:
            return response.status_code, None

    def get_vehicle_by_id(self, vehicle_id):
        """
        Retrieves a specific vehicle from the API by its ID.

        :param vehicle_id: Vehicle's ID
        :return: Tuple (status_code, JSON object of the vehicle) or (status_code, None)
        """
        specific_url = f"{self.url}{vehicle_id}/"
        response = requests.get(url=specific_url)
        if response.status_code == 200:
            vehicle_info = response.json()
            vehicle = VehicleFactory.create_vehicle(vehicle_info)
            return response.status_code, vehicle
        else:
            return response.status_code, None

    def delete_vehicle_by_id(self, vehicle_id):
        """
        Deletes a vehicle from the API by its ID.

        :param vehicle_id: Vehicle's ID
        :return: status_code
        """
        specific_url = f"{self.url}{vehicle_id}/"
        response = requests.delete(url=specific_url)
        return response.status_code

    def create_vehicle(self, data):
        """
        Creates a new vehicle in the API.

        :param data: dictionary of data
        :return: status_code, vehicle
        """
        if set(data.keys()) != set(FIELDS):
            raise Exception("Error in data format. The dictionary must include these fields:" + str(FIELDS))
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=self.url, data=json.dumps(data), headers=headers)
        if response.status_code == 201:
            return response.status_code, VehicleFactory.create_vehicle(data)
        else:
            return response.status_code, None

    def update_vehicle(self, vehicle_id, data):
        """
        Updates a specific vehicle in the API by its ID.

        :param vehicle_id: Vehicle's ID
        :param data: dictionary of data to update
        :return: status_code, vehicle
        """
        if set(data.keys()) != set(FIELDS):
            raise Exception("Error in data format. The dictionary must include these fields:" + str(FIELDS))
        specific_url = f"{self.url}{vehicle_id}/"
        response = requests.put(url=specific_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            return response.status_code, VehicleFactory.create_vehicle(data)
        else:
            return response.status_code, None
