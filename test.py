import unittest
from app.main import app  # Import your Flask app from your main.py (adjust as needed)
from flask import json

class FlaskAppTestCase(unittest.TestCase):
    # Set up the Flask test client
    def setUp(self):
        self.app = app.test_client()  # Use Flask's test client for simulating requests
        self.app.testing = True  # Enable testing mode for the Flask app

    # Test the root endpoint (assuming your app has a home route)
    def test_home_page(self):
        response = self.app.get("/")  # Send a GET request to the home route
        self.assertEqual(response.status_code, 200)  # Assert that the status code is 200
        self.assertIn(b"Welcome to the Image Compressor", response.data)  # Check if the response contains expected text

    # Test another endpoint (for example, an image compression endpoint)
    def test_compress_image(self):
        with open('test_image.jpg', 'rb') as img:  # Ensure you have a test image in the project
            response = self.app.post(
                '/compress',  # Adjust to your actual endpoint
                data={'image': img},
                content_type='multipart/form-data'
            )
            self.assertEqual(response.status_code, 200)  # Check if the status code is 200
            self.assertIn(b"Image compressed successfully", response.data)  # Check if expected message appears

    # Test non-existent route (to check error handling)
    def test_invalid_route(self):
        response = self.app.get("/non-existent-route")
        self.assertEqual(response.status_code, 404)  # Assert that it returns a 404 error

if __name__ == "__main__":
    unittest.main()
