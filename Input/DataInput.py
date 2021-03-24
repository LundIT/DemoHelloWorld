from ProcessAdminRestApi.models.process_admin_model import DependencyAnalysisMixin
from generic_app.models import *
from generic_app.submodels.DemoHelloWorld.Input.Period import Period


class DataInput(DependencyAnalysisMixin, Model):
    id = IntegerField(primary_key=True)
    period = ForeignKey(to=Period, on_delete=CASCADE)
    data = IntegerField()
