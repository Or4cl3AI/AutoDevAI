```python
class Memory:
    def __init__(self):
        self.memory = {}

    def store(self, key, value):
        self.memory[key] = value

    def retrieve(self, key):
        return self.memory.get(key, None)

    def update(self, key, value):
        if key in self.memory:
            self.memory[key] = value

    def delete(self, key):
        if key in self.memory:
            del self.memory[key]

    def clear(self):
        self.memory.clear()
```