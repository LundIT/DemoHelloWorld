from generic_app.models import *
from generic_app import models


class Output(Model):
    id = models.AutoField(primary_key=True)
    text = TextField()

    def __str__(self):
        return self.text
