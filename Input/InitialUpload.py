from generic_app.models import *

import pandas as pd
from generic_app.submodels.DemoHelloWorld.Input.SingleCharInput import SingleCharInput


class InitialUpload(UploadModelMixin):
    id = AutoField(primary_key=True)
    hello_world_upload_file = FileField(max_length=300)

    def update(self):
        input_data = pd.read_excel(self.hello_world_upload_file)
        for index, row in input_data.iterrows():
            singe_char_input = SingleCharInput(character=row['character'])
            singe_char_input.save()
