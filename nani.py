from datetime import datetime


class Foo:
    def __init__(self, n):
        self.id = n
        self.date = datetime.now()

    @property
    def consult_id(self):
        return id

    def consult_day(self):
        return self.date.day
