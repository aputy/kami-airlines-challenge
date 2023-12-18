from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Airplane
from .serializers import AirplaneSerializer

# Create your tests here.

# AirplaneModel Testcase
class TestAirplaneModel(TestCase):
    def test_fuel_consumption_per_minute(self):
        # Create an instance of Airplane with specific values
        airplane = Airplane(plane_id=1, passenger_assumptions=100)

        # Calculate the expected result based on your formula
        expected_result = 0.80 * airplane.plane_id + 0.002 * airplane.passenger_assumptions

        # Test that the actual result matches the expected result
        self.assertEqual(airplane.fuel_consumption_per_minute(), expected_result)

    def test_fuel_tank_capacity(self):
        # Create an instance of Airplane with specific values
        airplane = Airplane(plane_id=1, passenger_assumptions=100)

        # Calculate the expected result based on your formula
        expected_result = 200 * airplane.plane_id

        # Test that the actual result matches the expected result
        self.assertEqual(airplane.fuel_tank_capacity(), expected_result)

    def test_max_minutes_fly(self):
        # Create an instance of Airplane with specific values
        airplane = Airplane(plane_id=1, passenger_assumptions=100)

        # Calculate the expected result based on your formula
        expected_result = airplane.fuel_tank_capacity() / airplane.fuel_consumption_per_minute()

        # Test that the actual result matches the expected result
        self.assertEqual(airplane.max_minutes_fly(), expected_result)

# AirplaneSerializer Testcase
class TestAirplaneSerializer(APITestCase):
    def setUp(self):
        # Create an Airplane object with some test data
        self.airplane_data = {
            'plane_id': 3,
            'passenger_assumptions': 150,
            # Add other fields as needed for your Airplane model
        }
        self.airplane = Airplane.objects.create(**self.airplane_data)

    def test_airplane_serializer(self):
        # Serialize the Airplane object
        serializer = AirplaneSerializer(instance=self.airplane)

        # Verify the serialized data
        expected_data = {
            'plane_id': 3,
            'passenger_assumptions': 150,
            'fuel_consumption_per_minute': round(self.airplane.fuel_consumption_per_minute(), 2),
            'max_minutes_fly': round(self.airplane.max_minutes_fly(), 2),
            # Add other expected fields based on your model and serializer
        }

        self.assertEqual(serializer.data, expected_data)

# AirplaneView Testcase
class TestAirplaneViewSet(APITestCase):
    def setUp(self):
        # Create some instances of Airplane for testing
        Airplane.objects.create(plane_id=1, passenger_assumptions=100)
        Airplane.objects.create(plane_id=2, passenger_assumptions=150)

    def test_list_view(self):
        # Test the list endpoint
        url = reverse('airplane-list')  # Assuming you have a proper URL pattern configured
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Assuming you have 2 instances in the database

        # Add more assertions based on your expected data format
        self.assertIn('plane_id', response.data[0])
        self.assertIn('max_minutes_fly', response.data[0])
        self.assertIn('fuel_consumption_per_minute', response.data[0])