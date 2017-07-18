from test.api import TestApi


class Test(TestApi):
    def test(self):
        self.request("POST", "/user", data={
            "username": "bluice",
            "password": "123456",
            "nickname": "无常"
        }
                     )
