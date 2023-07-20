```python
import unittest
from ai_agent.internet_access import access_internet

class TestInternetAccess(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.example.com"
        self.query = "AI research papers"

    def test_access_internet(self):
        response = access_internet(self.url)
        self.assertIsNotNone(response)

    def test_search_query(self):
        results = access_internet(self.query)
        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)

if __name__ == '__main__':
    unittest.main()
```