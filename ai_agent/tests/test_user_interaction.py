```python
import unittest
from ai_agent import user_interaction

class TestUserInteraction(unittest.TestCase):

    def setUp(self):
        self.user_interaction = user_interaction.UserInteraction()

    def test_process_input(self):
        user_input = "Hello, AI!"
        expected_output = "Hello, AI!"
        self.assertEqual(self.user_interaction.process_input(user_input), expected_output)

    def test_generate_response(self):
        user_input = "Hello, AI!"
        response = self.user_interaction.generate_response(user_input)
        self.assertIsNotNone(response)

    def test_user_input_field(self):
        user_input = "Hello, AI!"
        self.user_interaction.user_input_field = user_input
        self.assertEqual(self.user_interaction.user_input_field, user_input)

    def test_agent_response_field(self):
        response = "Hello, User!"
        self.user_interaction.agent_response_field = response
        self.assertEqual(self.user_interaction.agent_response_field, response)

if __name__ == '__main__':
    unittest.main()
```