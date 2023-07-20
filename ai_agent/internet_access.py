```python
import requests

class InternetAccess:
    def __init__(self):
        self.session = requests.Session()

    def access_internet(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")

    def close_session(self):
        self.session.close()
```