```python
import unittest
from ai_agent.code_generator import generate_code

class TestCodeGenerator(unittest.TestCase):

    def setUp(self):
        self.user_input = "Generate a Python function to add two numbers"
        self.expected_output = "def add_two_numbers(num1, num2):\n    return num1 + num2"

    def test_generate_code(self):
        agent_response = generate_code(self.user_input)
        self.assertEqual(agent_response, self.expected_output)

if __name__ == '__main__':
    unittest.main()
```