from qiniu import Auth
from conf import conf


class ServiceQiNiu(object):
    def __init__(self):
        c = conf()
        self.access_key = c["qiniu"]["access_key"]
        self.secret_key = c["qiniu"]["secret_key"]
        self.bucket = c["qiniu"]["bucket"]
        self.host = c["qiniu"]["host"]

    def get_upload_token(self, file_name: str) -> (str, str):
        q = Auth(self.access_key, self.secret_key)
        token = q.upload_token(self.bucket, file_name, 3600)
        return token, f"{self.host}/{file_name}"

if __name__ == "__main__":
    print(ServiceQiNiu().get_upload_token("001.jpg"))
