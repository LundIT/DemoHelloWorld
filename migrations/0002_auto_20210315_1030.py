# Generated by Django 3.0.13 on 2021-03-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SingleCharInput',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('character', models.TextField(max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='initialupload',
            name='hello_world_upload_file',
            field=models.FileField(default=2, max_length=300, upload_to=''),
            preserve_default=False,
        ),
    ]
