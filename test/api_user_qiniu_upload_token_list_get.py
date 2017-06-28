from test.api import TestApi


class Test(TestApi):
    def test(self):
        self.request("GET", "/user/37/qiniu_upload_token?file_name=me.png")
