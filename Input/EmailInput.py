from ProcessAdminRestApi.models.process_admin_model import DependencyAnalysisMixin
from generic_app.models import *
from generic_app.submodels.DemoHelloWorld.Input.Period import Period


class EmailInput(DependencyAnalysisMixin, Model):
    id = IntegerField(primary_key=True)
    period = ForeignKey(to=Period, on_delete=CASCADE)
    name = TextField()
    email = TextField()

    def __str__(self):
        return str(self.name)
