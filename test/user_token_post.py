from test.api import TestApi


class Test(TestApi):
    def test(self):
        self.request("POST", "/user_token",
                     data={
                         "username": "bluice",
                         "password": "123456",
                     })
