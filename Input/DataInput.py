from ProcessAdminRestApi.models.process_admin_model import DependencyAnalysisMixin
from generic_app.models import *
from generic_app.submodels.DemoHelloWorld.Input.Period import Period


class DataInput(DependencyAnalysisMixin, Model):
    id = AutoField(primary_key=True)
    data_id = IntegerField()
    period = ForeignKey(to=Period, on_delete=CASCADE)
    data = IntegerField()
















    def directly_dependent_entries(self):
        from generic_app.submodels.DemoHelloWorld.Calculation.Aggregation import Aggregation
        from generic_app.submodels.DemoHelloWorld.Input.EmailInput import EmailInput

        email_input = EmailInput.objects.filter(period=self.period, email_id=self.data_id).first()

        report = Aggregation.objects.filter(name=email_input.name)

        report.calculate()
