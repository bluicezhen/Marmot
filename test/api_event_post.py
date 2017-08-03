from test.api import TestApi


class Test(TestApi):
    def test(self):
        self.request("POST", "/event",
                     data={
                         "title": "Test Event 01",
                         "desc": "Test Event 01",
                         "time_begin": 1399849081,
                         "time_end": 1299849081
                     })
