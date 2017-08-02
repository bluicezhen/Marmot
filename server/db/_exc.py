class ExceptionDB(Exception):
    def __init__(self, e_type: str, field: str=None):
        self.type = e_type
        self.field = field

    def __str__(self):
        return repr(f"Database Error: {self.type}")
