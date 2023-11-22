from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from REST.models import Vehicle


class VehiclesAPITest(TestCase):
    def setUp(self):
        # Initializing an APIClient for making requests and creating a vehicle object for testing
        self.client = APIClient()
        self.vehicle = Vehicle.objects.create(
            id=1,
            latitude=40.7128,
            longitude=-74.0060
        )

    def test_get_single_vehicle(self):
        # Test retrieving a single vehicle by ID (1) and checking for a successful response
        response = self.client.get(reverse('vehicle-api-id', kwargs={'vehicle_id': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_vehicles(self):
        # Test fetching all vehicles and checking for a successful response
        response = self.client.get(reverse('vehicle-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vehicle(self):
        # Test creating a new vehicle with valid data and check for a successful response
        data = {
            'id': 2,
            'latitude': 37.7749,
            'longitude': -122.4194
        }
        response = self.client.post(reverse('vehicle-api'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_vehicle(self):
        # Test creating a vehicle with invalid latitude data and ensure it returns an error response
        data = {
            'id': 2,
            'latitude': 'invalid_latitude',  # Invalid latitude data
            'longitude': -122.4194
        }
        response = self.client.post(reverse('vehicle-api'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_vehicle(self):
        # Test updating the vehicle with ID 1 using specific latitude and longitude values
        response = self.client.put(reverse('vehicle-api-id', kwargs={'vehicle_id': 1}),
                                   {'id': 1, 'latitude': 34.0522, 'longitude': -118.2437}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vehicle(self):
        # Test deleting the vehicle with ID 1 and checking for a successful response
        response = self.client.delete(reverse('vehicle-api-id', kwargs={'vehicle_id': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_nonexistent_vehicle(self):
        # Test deleting a non-existent vehicle (ID 100) and ensure it returns an error response
        response = self.client.delete(reverse('vehicle-api-id', kwargs={'vehicle_id': 100}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
