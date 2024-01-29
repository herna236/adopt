import unittest
from your_application import app
from flask_testing import TestCase
from forms import AddPetForm

class TestAddPetForm(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_valid_form(self):
        """Test form submission with valid data."""
        with self.client:
            response = self.client.post('/add', data={
                'name': 'Buddy',
                'species': 'Dog',
                'photo_url': 'http://www.example.com/image.jpg',
                'age': 5,
                'notes': 'Friendly and playful.'
            }, follow_redirects=True)
            self.assertIn(b'Buddy added.', response.data)

    def test_invalid_url(self):
        """Test form submission with invalid URL."""
        with self.client:
            response = self.client.post('/add', data={
                'name': 'Fluffy',
                'species': 'Cat',
                'photo_url': 'www.example.com/image.jpg',  # Invalid URL missing protocol
                'age': 3,
                'notes': 'Likes to sleep.'
            }, follow_redirects=True)
            self.assertIn(b'Invalid URL.', response.data)

   

if __name__ == '__main__':
    unittest.main()
