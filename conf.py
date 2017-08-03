debug = True


def conf():
    if debug:
        return {
            "token_validity": 60 * 60,
            "qiniu": {
                "access_key": "t7eyEfX6fXJOmG3b_-6B8lgLXwmShOLcmcIeYMSQ",
                "secret_key": "3m5rOjW3P3859hralq9pAlHrQNV58S2DSIOZR8yY",
                "bucket": "marmot-test",
                "host": "http://ohv2dx6w7.bkt.clouddn.com"
            }
        }
