from generic_app.models import *

import pandas as pd
from generic_app.submodels.DemoHelloWorld.Input.EmailInput import EmailInput
from generic_app.submodels.DemoHelloWorld.Input.Period import Period
from generic_app.submodels.DemoHelloWorld.Calculation.Aggregation import Aggregation

class EmailUpload(UploadModelMixin):
    id = AutoField(primary_key=True)
    period = ForeignKey(to=Period, on_delete=CASCADE)
    email_file = FileField(max_length=300)

    def update(self):
        input_file = pd.read_excel(self.email_file)
        for index, row in input_file.iterrows():
            email_input = EmailInput(id=row['id'], period=self.period, name=row['name'], email=row['email'])
            email_input.save()

    def __str__(self):
        return str(self.name)
