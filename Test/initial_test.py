import pathlib


from unittest import TestCase
#from django.test import TestCase
from generic_app.submodels.DemoHelloWorld.Input.InitialUpload import InitialUpload
from generic_app.submodels.DemoHelloWorld.Input.SingleCharInput import SingleCharInput
from generic_app.submodels.DemoHelloWorld.Output.Output import Output


class InitialTest(TestCase):

    def setUp(self) -> None:
        path = pathlib.Path(__file__).parent.absolute().__str__()
        path = path + "/../UploadFiles/"

        Output.objects.all().delete()
        SingleCharInput.objects.all().delete()
        InitialUpload.objects.all().delete()

        self.initial_upload = InitialUpload(hello_world_upload_file=path + "UploadFile.xlsx")
        self.initial_upload.save()

    def test(self):
        print("Start test")
