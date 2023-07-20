```python
import unittest
from ai_agent.memory import Memory

class TestMemory(unittest.TestCase):

    def setUp(self):
        self.memory = Memory()

    def test_store_memory(self):
        user_input = "Hello, AI!"
        self.memory.store_memory(user_input)
        self.assertEqual(self.memory.recall_memory(), user_input)

    def test_recall_memory(self):
        user_input = "How are you, AI?"
        self.memory.store_memory(user_input)
        recalled_memory = self.memory.recall_memory()
        self.assertEqual(recalled_memory, user_input)

    def test_clear_memory(self):
        user_input = "Goodbye, AI!"
        self.memory.store_memory(user_input)
        self.memory.clear_memory()
        self.assertIsNone(self.memory.recall_memory())

if __name__ == '__main__':
    unittest.main()
```