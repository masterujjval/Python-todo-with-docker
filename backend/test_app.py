import unittest
from application import app  # adjust if your app is defined elsewhere

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Todo', response.data)  # adjust based on expected content

    def test_api_todos(self):
        response = self.app.get('/api/todos')  # adjust route as needed
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

if __name__ == '__main__':
    unittest.main()
