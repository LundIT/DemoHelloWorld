import pathlib
from datetime import datetime

from unittest import TestCase
#from django.test import TestCase

from generic_app.submodels.DemoHelloWorld.Calculation.Aggregation import Aggregation
from generic_app.submodels.DemoHelloWorld.Upload.EmailUpload import EmailUpload
from generic_app.submodels.DemoHelloWorld.Upload.DataUpload import DataUpload
from generic_app.submodels.DemoHelloWorld.Input.Period import Period


class InitialTest(TestCase):

    def setUp(self) -> None:
        path = pathlib.Path(__file__).parent.absolute().__str__()
        path = path + "/../UploadFiles/"

        Period.objects.all().delete()
        Aggregation.objects.all().delete()
        self.period = Period(name="Test Period", date=datetime(year=2020, month=12, day=31))
        self.period.save()

        self.email_upload = EmailUpload(period=self.period, email_file=path + "EmailFile.xlsx")
        self.email_upload.save()

        self.data_upload = DataUpload(period=self.period, data_file=path + "DataFile.xlsx")
        self.data_upload.save()

    def test(self):
        print("Start test")
