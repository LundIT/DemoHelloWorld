from ProcessAdminRestApi.models.process_admin_model import DependencyAnalysisMixin
from generic_app import models
from generic_app.models import *
from generic_app.submodels.DemoHelloWorld.Output.Output import Output


class SingleCharInput(DependencyAnalysisMixin, Model):
    id = models.AutoField(primary_key=True)
    character = TextField(max_length=1)

    def directly_dependent_entries(self):
        single_chars = SingleCharInput.objects.all()
        outputs = Output.objects.all()

        chars = ""
        for single_char in single_chars:
            chars += single_char.character

        if outputs.count() == 0:
            output = Output(text=chars)
        else:
            output = outputs.first()
            output.text = chars

        output.save()
        return []

