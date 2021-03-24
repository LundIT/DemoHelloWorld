from datetime import datetime
from io import BytesIO

import xlsxwriter
from django.core.files import File

from ProcessAdminRestApi.models.process_admin_model import DependencyAnalysisMixin
from django.db.models import Index, Sum, BooleanField

from generic_app.models import *
from generic_app.submodels.DemoHelloWorld.Input.DataInput import DataInput
from generic_app.submodels.DemoHelloWorld.Input.EmailInput import EmailInput
from generic_app.submodels.DemoHelloWorld.Input.Period import Period
import pandas as pd


def create_excel_file(data_frames, sheet_names=None):
    if sheet_names is None:
        sheet_names = ['Sheet']
    excel_file = BytesIO()
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    df: pd.DataFrame
    for df, sheet_name in zip(data_frames, sheet_names):
        df.to_excel(writer, sheet_name=sheet_name, merge_cells=True, freeze_panes=(1, 1))
        money_fmt = writer.book.add_format({'num_format': '#,##0.00'})
        worksheet: xlsxwriter.worksheet.Worksheet = writer.sheets[sheet_name]

    writer.save()
    writer.close()
    excel_file.seek(0)
    return excel_file


class Aggregation(DependencyAnalysisMixin, CalculatedModelMixin, Model):
    id = AutoField(primary_key=True)
    period = ForeignKey(to=Period, on_delete=CASCADE)
    name = TextField()
    value = IntegerField()
    file_to_send = FileField(max_length=300)

    class Meta:
        indexes = [
            Index(fields=['period', 'name'])
        ]

    defining_fields = ['period', 'name']

    def get_selected_key_list(self, key: str) -> list:
        if key == 'period':
            return Period.objects.all()
        if key == 'name':
            return list(EmailInput.objects.filter(period=self.period).values_list('name', flat=True).distinct())

    def calculate(self):
        email_ids = list(
            EmailInput.objects.filter(period=self.period, name=self.name).values_list('email_id', flat=True))
        data_sum = DataInput.objects.filter(period=self.period, data_id__in=email_ids).aggregate(Sum('data'))[
            'data__sum']
        self.value = data_sum

        data_frame = pd.DataFrame.from_records(
            DataInput.objects.filter(period=self.period, data_id__in=email_ids).values())
        excel = create_excel_file(data_frames=[data_frame], sheet_names=['FilteredDataInput'])
        date_string = datetime.now().strftime("%Y-%m-%d_%H-%M.%S")
        self.file_to_send.save(f'{self.name}_DatInput_{date_string}.xlsx', content=File(excel))
