# Generated by Django 3.1.1 on 2020-09-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendreq', '0001_auto_20200906_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrequest',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('closed', 'closed'), ('in_process', 'in process')], default='open', max_length=40),
        ),
    ]
