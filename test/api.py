import json
import unittest
from io import StringIO
from pprint import pprint
from server import create_app


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def request(self, method: str, url: str, data: dict=None, user_uuid: str="37"):
        print(f"{method} {url}")
        headers = {
            "Content-Type": "application/json",
            "User-UUID": user_uuid,
            "Token": "Marmot"
        }
        if method == "GET":
            self.request = self.app.get(
                url,
                headers=headers,
                input_stream=StringIO(json.dumps(data))
            )
        elif method == "POST":
            self.request = self.app.post(
                url,
                headers=headers,
                input_stream=StringIO(json.dumps(data))
            )
        print(self.request._status)
        print(self.request.headers)
        try:
            pprint(json.loads(self.request.data.decode("utf-8")))
        except json.JSONDecodeError:
            print("{}".format(self.request.data.decode("utf-8")))
