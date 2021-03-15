from generic_app.models import *

class SingleCharacter(Model):
    id=AutoField(primary_key=True)
    text = TextField(max_length=1)