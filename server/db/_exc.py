class DBException(Exception):
    def __init__(self, type: str, field: str=None):
        self.type = type
        self.field = field

    def __str__(self):
        return repr(f"Database Error: {self.type}")
