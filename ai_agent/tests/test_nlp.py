```python
import unittest
from ai_agent.nlp import process_input, generate_response

class TestNLP(unittest.TestCase):

    def setUp(self):
        self.user_input = "Hello AI"
        self.agent_response = "Hello User"

    def test_process_input(self):
        result = process_input(self.user_input)
        self.assertIsNotNone(result)

    def test_generate_response(self):
        result = generate_response(self.user_input)
        self.assertEqual(result, self.agent_response)

if __name__ == '__main__':
    unittest.main()
```