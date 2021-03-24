from generic_app.models import *

import pandas as pd

from generic_app.submodels.DemoHelloWorld.Calculation.Aggregation import Aggregation
from generic_app.submodels.DemoHelloWorld.Input.DataInput import DataInput
from generic_app.submodels.DemoHelloWorld.Input.Period import Period


class DataUpload(UploadModelMixin):
    id = AutoField(primary_key=True)
    period = ForeignKey(to=Period, on_delete=CASCADE)
    data_file = FileField(max_length=300)

    def update(self):
        input_data = pd.read_excel(self.data_file)
        for index, row in input_data.iterrows():
            data_input = DataInput(data_id=row['id'], period=self.period, data=row['data'])
            data_input.save()
        Aggregation.create(period=[self.period])
