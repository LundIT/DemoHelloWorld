from generic_app.models import *


class Period(Model):
    id = AutoField(primary_key=True)
    name = TextField()
    date = DateTimeField()

    def __str__(self):
        return str(self.name) + " " + str(self.id)